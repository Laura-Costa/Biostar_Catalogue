c         *********************************************
c         *                                           *
c         *  Astrom.for - programa para auxiliar no   *
c         *  planejamento de noites de observação.    * 
c         *                                           *
c         *  Eduardo Fernandez del Peloso             *
c         *  versão 2.0 - 17/03/97                    *
c         *                                           *
c         *********************************************
c
c
c         O arquivo de entrada, chamado 'estrelas.dat' deve conter as seguintes informações,
c         obrigatoriamente na ordem apresentada:
c
c         1) Data da observação: dia, mês e ano (com 4 algarismos).
c         2) Localização: latitude em graus, minutos e segundos precedida da letra 's' ou 'n' entre aspas simples.
c                         longitude em graus, minutos e segundo precedida da letra 'o' ou 'l' entre aspas simples.
c                         fuso em horas (+ para oeste de Greenwich, - para leste)
c         3) Ângulo do almicantarado que deseja calcular a hora de passagem, em graus.
c         4) Tempo sideral em Greenwich a zero horas (0h00) para o dia da observação, em horas
c            e minutos (vide anuário de efemérides astronômicas).                             
c         5) Lista de estrelas, composta por identificação numerica (HR, HD, ...), ascenção reta em horas, minutos e
c            segundos, declinação em graus, minutos e segundo (época 2000.0) e movimentos próprios anuais na ascenção
c            reta e declinacao (em segundos de arco).
c            A lista deve terminar com 9 zeros.
c                                                                                          
c
c         Exemplo de arquivo 'estrelas.dat':
c
c         24 3 1997
c         's' 30 09 00 'o' 70 48 00 4
c         30
c         12 00
c         3018 7 45 34.8 -34 10 23 -0.293 1.662 
c         5459 14 39 36.2 -60 50 7 -3.608 0.712
c         5802 15 36 29.5 10 0 36 0.043 -0.132
c         0 0 0 0 0 0 0 0 0


    
      REAL latdeg, latmin, latsec, longdeg, longmin, longsec, fuso, data
      INTEGER hrinteiro, tlnh, tlnm, tl1h, tl1m, tlculmh, tlculmm, tl2h,
     +tl2m, tloh, tlom, dia, mes, ano,ascretah,ascretam,ascretas,dech,
     +decm,decs
      REAL longgraus, latgraus, longhora, latrad,pmascreta,pmdec
      REAL limite, dec, ascreta, tsl1, tsl2, tl1, tl2
      REAL ascretadeg, ascretamin, ascretasec, decdeg, decmin, decsec
      REAL tsg, tsghora, tsgmin, tsln, tslo
      REAL x, y, z, t2, deltaascreta, deltadec, t, decgraus
      CHARACTER*1 latsign, longsign
           
      OPEN (1, FILE = 'estrelas.dat', STATUS = 'OLD')
      OPEN (2, FILE = 'obsrun.dat', STATUS = 'UNKNOWN')
      
      READ (1,*) dia, mes, ano
      READ (1,*) latsign, latdeg, latmin, latsec, longsign, longdeg, 
     +   longmin, longsec, fuso
                              

      
                              
c     ******** Calcula LONGITUDE em GRAUS (decimais) **************                         
      longgraus = longdeg + (longmin/60.0) + (longsec/3600.0)
      IF ((longsign.eq.'L').or.(longsign.eq.'l'))
     +   longgraus = 360.0 - longgraus
      
      
c     ******** Calcula LONGITUDE em HORAS (decimais) **************        
      longhora = longgraus / 15.0 
      

c     ******** Calcula LATITUDE em GRAUS (decimais) ***************     
      latgraus = latdeg + (latmin/60.0) + (latsec/3600.0)
      IF ((latsign.eq.'S').or.(latsign.eq.'s'))
     +   latgraus = - latgraus
                      
                     
c     ******** Calcula LATITUDE em RADIANOS ***********************                 
      latrad = latgraus / 57.29577951                 
                          
      READ (1,*) limite, tsghora, tsgmin
      
      
c     ******** Calcula o ângulo do almicantarado desejado em RADIANOS *********** 
      limite = limite / 57.29577951
      
      
c     ******** Tempo sideral em Greenwich a zero horas em HORAS DECIMAIS ********      
      tsg = tsghora + (tsgmin/60.0)
                  
  
      WRITE (2,30) dia, mes, ano, INT(latdeg), INT(latmin), INT(latsec),
     +latsign, INT(longdeg), INT(longmin), INT(longsec), longsign, fuso 
               
      WRITE (2,*) ' '         
               
      WRITE (2,*) 
     +'Estrela    nascer   almic.1   culm.   almic.2   ocaso      R.A.
     +      DEC'
      
1111  continue  
      
      




      
c     ******* Lê estrelas ********                           
      READ (1,*) hr, ascretadeg, ascretamin, ascretasec, decdeg, decmin,
     +decsec, pmascreta, pmdec
     
c     ******* Sai quando HR=0 *******
      IF (hr.eq.0) goto 2222
        
c     ******* Ascenção reta em HORAS (decimais) *******              
      ascreta = ascretadeg + (ascretamin/60.0) + (ascretasec/3600.0)
         
c     ******* Declinação em RADIANOS ***********    
      IF (decdeg.lt.0.0)
     +dec = decdeg - (decmin/60.0) - (decsec/3600.0)
      IF (decdeg.ge.0.0)
     +dec = decdeg + (decmin/60.0) + (decsec/3600.0)            
      dec = dec / 57.29577951 
                                 
c     ***** CORRIGE precessão (ascenção reta E declinção) *********                              
      IF (mes.eq.1) data = dia
      IF (mes.eq.2) data = 31 + dia
      IF (mes.eq.3) data = 59 + dia
      IF (mes.eq.4) data = 90 + dia
      IF (mes.eq.5) data = 120 + dia
      IF (mes.eq.6) data = 151 + dia
      IF (mes.eq.7) data = 181 + dia
      IF (mes.eq.8) data = 212 + dia
      IF (mes.eq.9) data = 243 + dia
      IF (mes.eq.10) data = 273 + dia
      IF (mes.eq.11) data = 304 + dia
      IF (mes.eq.12) data = 334 + dia
      data = data / 365.0
      data = ano + data
      t2 = (((2000.0+data)/2.0)-1900.0)/100.0
      x = 3.07234 + (0.00186*t2)
      y = 20.0468 - (0.0085*t2)
      z = y/15.0
      t = data - 2000.0
c     ****** Correção da ASCENÇÃO RETA calculada em GRAUS e dividida por 15.00 para obtermos correção em HORAS DECIMAIS *********       
      deltaascreta = (0.0042 * t * (x + (z * sin(ascreta*
     +0.261799388) * tan(dec))))/15.0
c     ****** Ascenção reta PRECESSIONADA e CORRIGIDA por mov. próprios em HORAS DECIMAIS **********
      ascreta=ascreta+deltaascreta+((data-2000.0)*(pmascreta/(3600*15)))
c     ****** Correção da DECLINAÇÃO calculada em GRAUS e dividida por 52.29577951 para obtermos correção em RADIANOS **********
      deltadec = 0.00028 * t * y * cos(ascreta*
     +0.261799388) / 57.29577951
c     ****** Declinação PRECESSIONADA e CORRIGIDA por movimentos próprios em RADIANOS **********
      dec=dec+deltadec+((data-2000.0)*(pmdec/206264.8063))
                          
c     ****** Calcula A.R. (ja precessionada) em horas, minutos, segundos *******
      ascretah=INT(ascreta)
      ascretam=INT((ascreta-ascretah)*60.0)
      ascretas=INT((((ascreta-ascretah)*60.0)-ascretam)*60.0)
c     ****** Calcula DEC (ja precessionada) em graus, minutos, segundos ********
      decgraus=dec*57.29577951   
      dech=INT(decgraus)
      decm=INT((ABS(decgraus)-ABS(dech))*60.0)
      decs=INT((((ABS(decgraus)-ABS(dech))*60.0)-decm)*60.0)
      





           
      
c     ******** Se a estrela não passa pelo almicantarado faz tl1=tl2=0 e pula os cálculos de tl1 e tl2 *********      
      IF ((((sin(limite)- (sin(dec)*sin(latrad))) 
     +/ (cos(dec)*cos(latrad))).lt.(-1.0)).or.(((sin(limite)-
     +(sin(dec)*sin(latrad))) 
     +/ (cos(dec)*cos(latrad))).gt.1.0)) THEN
         tl1 = 0.0
         tl2 = 0.0
         goto 6666
      END IF
                                       

c     ********* Cálculo do tempo sideral local e tempo legal da 1a passagem pelo almicantarado ********
      tsl1 = 24.0-((acos((sin(limite)-(sin(dec)*sin(latrad)))
     +/ (cos(dec)*cos(latrad))))*3.819718634)+ascreta
      IF (tsl1.gt.24.0) tsl1 = tsl1 - 24.0
      IF (tsl1.lt.0.0) tsl1 = 24.0 + tsl1  
      IF ((tsl1-tsg+longhora).lt.0.0) tl1 = ((tsl1-tsg+longhora+24.0)
     +/1.0027379093)-fuso  
      IF ((tsl1-tsg+longhora).ge.0.0) tl1 = ((tsl1-tsg+longhora)
     +/1.0027379093)-fuso
      IF (tl1.lt.0.0) tl1 = 24.0 + tl1
      IF (tl1.gt.24.0) tl1 = tl1 - 24.0
 
c     ********* Cálculo do tempo sideral local e tempo legal da 2a passagem pelo almicantarado ********                           
      tsl2 = ((acos((sin(limite)-(sin(dec)*sin(latrad))) 
     +/ (cos(dec)*cos(latrad))))*3.819718634) + ascreta 
      IF (tsl2.gt.24.0) tsl2 = tsl2 - 24.0
      IF (tsl2.lt.0.0) tsl2 = 24.0 + tsl2  
      IF ((tsl2-tsg+longhora).lt.0.0) tl2 = ((tsl2-tsg+longhora+24.0)
     +/1.0027379093)-fuso           
      IF ((tsl2-tsg+longhora).ge.0.0) tl2 = ((tsl2-tsg+longhora)
     +/1.0027379093)-fuso
      IF (tl2.lt.0.0) tl2 = 24.0 + tl2
      IF (tl2.gt.24.0) tl2 = tl2 - 24.0
     
            
6666  continue        
            
                                 






C     ********* Se a estrela for circumpolar faz tln=tlo=0 e pula o cálculo de tempo legal de ocaso e nascimento ******** 
      IF ((((-tan(latrad))*(tan(dec))).lt.(-1.0)).or.
     +   (((-tan(latrad))*(tan(dec))).gt.(1.0))) THEN
         tln = 0.0
         tlo = 0.0
         goto 3333
      END IF      
      
c     ********* Cálculo do tempo legal de nascimento **********                           
      tsln = ascreta - (acos((-tan(latrad))*tan(dec))*3.819718634) 
      IF (tsln.lt.0.0) tsln = 24.0 + tsln
      IF (tsln.gt.24.0) tsln = tsln - 24.0
      IF ((tsln-tsg+longhora).lt.0.0) tln = ((tsln-tsg+longhora+24.0)
     +/1.0027379093)-fuso
      IF ((tsln-tsg+longhora).ge.0.0) tln = ((tsln-tsg+longhora)
     +/1.0027379093)-fuso
      IF (tln.lt.0.0) tln = 24.0 + tln
      IF (tln.gt.24.0) tln = tln - 24.0      
      
c     ********* Cálculo do tempo legal de ocaso *********          
      tslo = ascreta + (acos((-tan(latrad))*tan(dec))*3.819718634) 
      IF (tslo.lt.0.0) tslo = 24.0 + tslo
      IF (tslo.gt.24.0) tslo = tslo - 24.0
      IF ((tslo-tsg+longhora).lt.0.0) tlo = ((tslo-tsg+longhora+24.0)
     +/1.0027379093)-fuso 
      IF ((tslo-tsg+longhora).ge.0.0) tlo = ((tslo-tsg+longhora)
     +/1.0027379093)-fuso
      IF (tlo.lt.0.0) tlo = 24.0 + tlo
      IF (tlo.gt.24.0) tl0 = tlo - 24.0
      
3333  continue

                                 




c     ******** Se a estrela NÃO é circumpolar o tempo da culminação é a média dos tempos de nascimento e ocaso *******
      IF (tlo.ne.0.0) THEN
        IF (tlo.gt.tln) tlculm = (tln+tlo)/2.0
        IF (tlo.lt.tln) tlculm = (tln+tlo-24.0)/2.0
        IF (tlculm.lt.0.0) tlculm = 24.0 + tlculm
        IF (tlculm.gt.24.0) tlculm = tlculm - 24.0
      END IF
 
           
10    FORMAT (I7,5x,2I3,3x,2I3,3x,2I3,3x,2I3,3x,2I3,3X,3I3,3X,3I3) 
20    FORMAT (I7, 5x, ' circ.', 3x, 2I3, 3x,2I3, 3x, 2I3, 3x,
     +' circ.',3X,3I3,3X,3I3)  
30    FORMAT ('Data:',1x,I2,'/',I2,'/',I4,3x,'Latitude:',1x,I2,'o',I2,
     +'''',I2,'"',a1,3x,'Longitude:',1x,I3,'o',I2,'''',I2,'"',a1,3x,
     +'Fuso:',1x,F2.0)    
40    FORMAT (I7,5x,2I3,5x,'nao',4x,2I3,5x,'nao',4x,2I3,3X,3I3,3X,3I3)
50    FORMAT (I7,6x,'circ.',5x,'nao',5x,'circ.',5x,'nao',5x,'circ.',3X,
     +3I3,3X,3I3)  


c     ********* Se a estrela é circumpolar MAS passa pelo almicantarado o tempo de culminacao é a média dos tempos de passagem *****           
      IF ((tlo.eq.0.0).and.(tl1.ne.0.0).and.(tl2.gt.tl1))
     + tlculm = ((tl1+tl2)/2.0)
      IF ((tlo.eq.0.0).and.(tl1.ne.0.0).and.(tl2.lt.tl1))
     + tlculm = ((tl1+tl2-24.0)/2.0)  
      IF (tlculm.lt.0.0) tlculm = 24.0 + tlculm
      IF (tlculm.gt.24.0) tlculm = tlculm - 24.0

      
      
c     ********* Converte horas decimais em horas + minutos + segundos *********     
c     ** HR **      
      hrinteiro = INT(hr)
c     ** Tempo nascimento **      
      tlnh = INT(tln)
      tlnm = INT((tln-tlnh)*60.0)
c     ** Tempo almicantarado 1 **      
      tl1h = INT(tl1)
      tl1m = INT((tl1-tl1h)*60.0)
c     ** Tempo culminação **      
      tlculmh = INT(tlculm)
      tlculmm = INT((tlculm-tlculmh)*60.0)
c     ** Tempo almicantarado 2 **      
      tl2h = INT(tl2)
      tl2m = INT((tl2-tl2h)*60.0)
c     ** Tempo ocaso **      
      tloh = INT(tlo)
      tlom = INT((tlo-tloh)*60.0)

      
c     ******* Imprime os dados das estrelas no arquivo de saída *******
c     ** Não circumpolar E PASSA pelo almicantarado **
      IF ((tlo.ne.0.0).and.(tl1.ne.0.0))
     +WRITE (2,10) hrinteiro, tlnh, tlnm, tl1h, tl1m, tlculmh, tlculmm,
     +tl2h, tl2m, tloh, tlom, ascretah, ascretam, ascretas,
     +dech,decm,decs    
c     ** Circumpolar e PASSA pelo almicantarado **    
      IF ((tlo.eq.0.0).and.(tl1.ne.0.0))
     +WRITE (2,20) hrinteiro, tl1h, tl1m, tlculmh, tlculmm, tl2h, tl2m,
     +ascretah,ascretam,ascretas,dech,decm,decs  
c     ** Não circumpolar e NÃO PASSA pelo almicantarado **
      IF ((tlo.ne.0.0).and.(tl1.eq.0.0))
     +WRITE (2,40) hrinteiro, tlnh, tlnm, tlculmh, tlculmm, tloh, tlom,
     +ascretah,ascretam,ascretas,dech,decm,decs
c     ** Circumpolar e NAO PASSA pelo almicantarado **      
      IF ((tlo.eq.0.0).and.(tl1.eq.0.0))
     +WRITE (2,50) hrinteiro,ascretah,ascretam,ascretas,dech,decm,decs       
                     
      
      goto 1111
      
2222  continue    
             
      CLOSE (1)
      CLOSE (2)
      END