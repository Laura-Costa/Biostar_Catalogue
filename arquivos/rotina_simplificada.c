#include<stdio.h>
#include<math.h>

int main(){

    long double PI = 3.14159265358979323846264338327950288419716939937510;

    long double RAdeg = 243.90472242;
    long double DEdeg = -8.36823651;
    long double pmRA = 232.16;
    long double pmDE = -495.84;
    long double m = 3.07234;
    long double n = 20.0468;
    long double ep0 = 1991.25;
    long double ep1 = 2016;

    // correção de movimento próprio e precessão
    long double RAdeg_2016 = RAdeg + (m*15/3600 + (n/3600)*sin(RAdeg*PI/180)*tan(DEdeg*PI/180))*(ep1 - ep0) + (pmRA/(1000*3600))*(ep1 - ep0);
    long double DEdeg_2016 = DEdeg + (n/3600)*(cos(RAdeg*PI/180))*(ep1 - ep0) + (pmDE/(1000*3600))*(ep1 - ep0);

    printf("RAdeg = %.20Lf\n", RAdeg_2016);
    printf("DEdeg = %.20Lf\n", DEdeg_2016);

    return 0;
}