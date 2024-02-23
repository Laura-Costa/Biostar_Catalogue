#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include <quadmath.h>
typedef __float128 real;

// #define PI 3.14159265358979323846264338327950288419716939937510

void slDC2S(long double * V, long double * A, long double * B);
void slDMXV(long double ** DM, long double * VA, long double * VB);
void slDS2C(long double A, long double B, long double * V);
void slDEUL(char* ORDER, long double PHI, long double THETA, long double PSI, long double ** RMAT);
void PREC(int EP0, int EP1, long double ** RMATP);
void prece(int ep0, int ep1, long double* ra, long double* dec);

int main(){
     
    long double PI = 3.14159265358979323846264338327950288419716939937510;
    printf("PI: %.50Lf\n", PI);

    int ep1 = 2016;
    int ep0 = 2000;

    // converter RAdeg Hipparcos para radianos
    long double ra = 243.90472242 * PI / 180;    

    // converter DEdeg Hipparcos para radianos
    long double dec = -8.36823651 * PI / 180;

    // converter pmRA e pmDE Hipparcos para radianos
    long double pmRA = 232.16/(1000*3600) * PI / 180;
    long double pmDE = -495.84/(1000*3600) * PI / 180;
    
    // Corrigir movimento proprio
    ra += pmRA * (24.75);
    dec += pmDE * (24.75);

    // Corrigir precessao dos equinocios
    //prece(ep0, ep1, &ra, &dec);
    printf("ra = %.20Lf\ndec = %.20Lf\n", ra, dec);





    // Coordenadas Gaia
    long double ar_gaia = 243.90633606005997 * PI / 180;
    long double dr_gaia = -8.371641161548801 * PI / 180;

    printf("ar em radianos (Gaia): %.20Lf\n", ar_gaia);
    printf("dr em radianos (Gaia): %.20Lf\n", dr_gaia);

    long double difer_ra = abs(ar_gaia - ra)*3600*(180/PI);
    long double difer_dec = abs(dec - dr_gaia)*3600*(180/PI);

    printf("diferença ar em segundos de arco: %.50Lf\n", difer_ra);
    printf("diferença dr em segundos de arco: %.50Lf\n", difer_dec);

 
    return 0;
}

void prece(int ep0, int ep1, long double* ra, long double* dec){
    long double ** pm;
    long double * v1;
    long double * v2;

    pm = (long double**)malloc(3 * sizeof (*pm));
    for (int i=0; i<3; i++){
        *(pm+i) = (long double*)malloc(3 * sizeof(*(*(pm+i))));
    }
    v1 = (long double*)malloc(3 * sizeof(*v1));
    v2 = (long double*)malloc(3 * sizeof(*v2));

    // construir a matriz de precessao
    PREC(ep0, ep1, pm);

    // passar ra e dec para x, y e z
    slDS2C(*ra, *dec, v1);

    // precessionar coordenadas
    slDMXV(pm, v1, v2);

    // de volta para ra e dec
    slDC2S(v2, ra, dec);
}

void PREC(int EP0, int EP1, long double ** RMATP){
    long double AS2R = 0.484813681109535994 * pow(10, -5);
    long double T0 = (EP0-2000)/100;
    long double T = (EP1-EP0)/100.0;

    long double TAS2R = T*AS2R;
    long double W = 2306.2181 + (1.39656 - 0.000139 * T0) * T0;
    long double ZETA = (W+((0.30188 - 0.000344 * T0) + 0.017998 * T) * T) * TAS2R;
    long double Z = (W+((1.09468 + 0.000066 * T0) + 0.018203 * T) * T) * TAS2R;
    long double THETA = ((2004.3109 + (-0.85330 - 0.000217 * T0) * T0) + 
        ((-0.42665 - 0.000217 * T0) - 0.041833 * T) * T) * TAS2R;

    char* ORDER;
    ORDER = malloc(4 * sizeof(char));
    *(ORDER) = 'Z';
    *(ORDER+1) = 'Y';
    *(ORDER+2) = 'Z';
    *(ORDER+3) = '\0';

    slDEUL(ORDER, -ZETA, THETA, -Z, RMATP);   
}

void slDEUL(char* ORDER, long double PHI, long double THETA, long double PSI, long double ** RMAT){
    int J,I,L,N,K;
    long double RESULT[3][3];
    long double ROTN[3][3];
    long double WM[3][3];
    long double ANGLE,S,C,W;
    char AXIS;

    // inicializar a matriz RESULT
    for(J = 0; J < 3; J++){
        for(I = 0; I < 3; I++){
            if(J == I){
                RESULT[J][I] = 1;
            }
            else{
                RESULT[J][I] = 0;
            }
        }
    }

    // comprimento da string AXIS
    L = strlen(ORDER);    

    // ler cada caractere da string AXIS
    for (N = 1; N <= 3; N++){
        if (N <= L){

            // inicializar a matriz de rotacao corrente
            for(J = 0; J < 3; J++){
                for(I = 0; I < 3; I++){
                    if(J != I){
                        ROTN[J][I] = 0;
                    }
                    else{
                        ROTN[J][I] = 1;
                    }
                }
            }

            // escolher o angulo de Euler apropriado e calcular seno e cosseno
            if(N == 1){
                ANGLE = PHI;
            }
            else if(N == 2){
                ANGLE = THETA;
            }
            else{
                ANGLE = PSI;
            }
            S = sin(ANGLE);
            C = cos(ANGLE);

            // identificar o eixo
            AXIS = ORDER[N-1];

            if(AXIS == 'X' || AXIS == 'x' || AXIS == '1'){

                // matriz para rotacao em torno do eixo x
                ROTN[1][1] = C;
                ROTN[1][2] = S;
                ROTN[2][1] = -S;
                ROTN[2][2] = C;
            }
            else if(AXIS == 'Y' || AXIS == 'y' || AXIS == '2'){

                // matriz para rotacao em torno do eixo y
                ROTN[0][0] = C;
                ROTN[0][2] = -S;
                ROTN[2][0] = S;
                ROTN[2][2] = C;
            }
            else if(AXIS == 'Z' || AXIS == 'z' || AXIS == '3'){

                // matriz para rotacao em torno do eixo z
                ROTN[0][0] = C;
                ROTN[0][1] = S;
                ROTN[1][0] = -S;
                ROTN[1][1] = C;
            }
            else{
                // caractere irreconhecivel
                L = 0;
            }

            // aplicar a matriz de rotacao corrente (ROTN x RESULT)
            for(I = 0; I < 3; I++){
                for(J = 0; J < 3; J++){
                    W = 0;
                    for(K = 0; K < 3; K++){
                        W += ROTN[I][K] * RESULT[K][J]; 
                    }
                    WM[I][J] = W;
                }
            }

            // atualizar RESULT
            for(J = 0; J < 3; J++){
                for(I = 0; I < 3; I++){
                    RESULT[I][J] = WM[I][J];
                }
            }
        }
    }

    // copiar RESULT para RMAT
    for (I = 0; I < 3; I++){
        for(J = 0; J < 3; J++){
            (*((*(RMAT + I)) + J)) = RESULT[I][J];
        }
    }
}

void slDS2C(long double A, long double B, long double * V){
    long double COSB;

    COSB = cos(B);
    *(V + 0) = cos(A) * COSB;
    *(V + 1) = sin(A) * COSB;
    *(V + 2) = sin(B);
}

void slDMXV(long double ** DM, long double * VA, long double * VB){
    int I, J;
    long double W;
    long double VW[3];

    // matriz DM x vetor VA -> vetor VW
    for(J = 0; J < 3; J++){
        W = 0;
        for(I = 0; I < 3; I++){
            W += (*(*(DM + J)+I)) * (*(VA + I));
        }
        VW[J] = W;
    }

    // vetor VW -> vetor VB
    for(J = 0; J < 3; J++){
        *(VB + J) = VW[J];
    }
}

void slDC2S(long double * V, long double * A, long double * B){
    long double X, Y, Z, R;

    X = *(V + 0);
    Y = *(V + 1);
    Z = *(V + 2);
    R = sqrt(X*X+Y*Y);

    if(R == 0){
        *A = 0;
    }
    else{
        *A = atan2(Y, X);
    }

    if(Z == 0){
        *B = 0;
    }
    else{
        *B = atan2(Z, R);
    }
}