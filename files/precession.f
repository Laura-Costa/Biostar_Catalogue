


      IMPLICIT REAL *8 (A-H,O-Z)



      d2000=2.451545d6


      ep0=(dj-d2000)/365.25d0+2000.d0
      ep1=2000.d0

      aqui, corrige movimentos proprios em ar e dr
      antes de submeter

      call prece(ep0,ep1,ar,dr)


      end
      
      


      SUBROUTINE prece (EP0, EP1, RA, DC)
*+
*     - - - - - - -
*      P R E C E
*     - - - - - - -
*
*  Precession - either FK4 (Bessel-Newcomb, pre IAU 1976) or
*  FK5 (Fricke, post IAU 1976) as required.
*
*  Given:
*     SYSTEM     char   precession to be applied: 'FK4' or 'FK5'
*     EP0,EP1    dp     starting and ending epoch
*     RA,DC      dp     RA,Dec, mean equator & equinox of epoch EP0
*
*  Returned:
*     RA,DC      dp     RA,Dec, mean equator & equinox of epoch EP1
*
*  Called:    slDA2P, slPRBN, slPREC, slDS2C,
*             slDMXV, slDC2S
*
*  Notes:
*
*     1)  Lowercase characters in SYSTEM are acceptable.
*
*     2)  The epochs are Besselian if SYSTEM='FK4' and Julian if 'FK5'.
*         For example, to precess coordinates in the old system from
*         equinox 1900.0 to 1950.0 the call would be:
*             CALL slPRCE ('FK4', 1900D0, 1950D0, RA, DC)
*
*     3)  This routine will NOT correctly convert between the old and
*         the new systems - for example conversion from B1950 to J2000.
*         For these purposes see slFK45, slFK54, slF45Z and
*         slF54Z.
*
*     4)  If an invalid SYSTEM is supplied, values of -99D0,-99D0 will
*         be returned for both RA and DC.
*
*  P.T.Wallace   Starlink   20 April 1990
*
*  Copyright (C) 1995 Rutherford Appleton Laboratory
*  Copyright (C) 1995 Association of Universities for Research in Astronomy Inc.
*-

      IMPLICIT real*8 (a-h,o-z)
C     IMPLICIT NONE

C     CHARACTER SYSTEM*(*)
      DOUBLE PRECISION EP0,EP1,RA,DC

      DOUBLE PRECISION PM(3,3),V1(3),V2(3)
C     CHARACTER SYSUC*3

C     DOUBLE PRECISION slDA2P


C     SYSTEM='FK5'

*  Convert to uppercase and validate SYSTEM
C     SYSUC=SYSTEM

*     Generate appropriate precession matrix
         CALL PREC(EP0,EP1,PM)

*     Convert RA,Dec to x,y,z
         CALL slDS2C(RA,DC,V1)

*     Precess
         CALL slDMXV(PM,V1,V2)

*     Back to RA,Dec
         CALL slDC2S(V2,RA,DC)
C        RA=slDA2P(RA)



      END




      SUBROUTINE PREC (EP0, EP1, RMATP)
*+
*     - - - - -
*      P R E C
*     - - - - -
*
*  Form the matrix of precession between two epochs (IAU 1976, FK5)
*  (double precision)
*
*  Given:
*     EP0    dp         beginning epoch
*     EP1    dp         ending epoch
*
*  Returned:
*     RMATP  dp(3,3)    precession matrix
*
*  Notes:
*
*     1)  The epochs are TDB (loosely ET) Julian epochs.
*
*     2)  The matrix is in the sense   V(EP1)  =  RMATP * V(EP0)
*
*     3)  Though the matrix method itself is rigorous, the precession
*         angles are expressed through canonical polynomials which are
*         valid only for a limited time span.  There are also known
*         errors in the IAU precession rate.  The absolute accuracy
*         of the present formulation is better than 0.1 arcsec from
*         1960AD to 2040AD, better than 1 arcsec from 1640AD to 2360AD,
*         and remains below 3 arcsec for the whole of the period
*         500BC to 3000AD.  The errors exceed 10 arcsec outside the
*         range 1200BC to 3900AD, exceed 100 arcsec outside 4200BC to
*         5600AD and exceed 1000 arcsec outside 6800BC to 8200AD.
*         The SLALIB routine slPREL implements a more elaborate
*         model which is suitable for problems spanning several
*         thousand years.
*
*  References:
*     Lieske,J.H., 1979. Astron.Astrophys.,73,282.
*      equations (6) & (7), p283.
*     Kaplan,G.H., 1981. USNO circular no. 163, pA2.
*
*  Called:  slDEUL
*
*  P.T.Wallace   Starlink   23 August 1996
*
*  Copyright (C) 1996 Rutherford Appleton Laboratory
*  Copyright (C) 1995 Association of Universities for Research in Astronomy Inc.
*-

      IMPLICIT real*8 (a-h,o-z)

      DOUBLE PRECISION EP0,EP1,RMATP(3,3)

*  Arc seconds to radians
      DOUBLE PRECISION AS2R
      PARAMETER (AS2R=0.484813681109535994D-5)

      DOUBLE PRECISION T0,T,TAS2R,W,ZETA,Z,THETA



*  Interval between basic epoch J2000.0 and beginning epoch (JC)
      T0 = (EP0-2000D0)/100D0

*  Interval over which precession required (JC)
      T = (EP1-EP0)/100D0

*  Euler angles
      TAS2R = T*AS2R
      W = 2306.2181D0+(1.39656D0-0.000139D0*T0)*T0

      ZETA = (W+((0.30188D0-0.000344D0*T0)+0.017998D0*T)*T)*TAS2R
      Z = (W+((1.09468D0+0.000066D0*T0)+0.018203D0*T)*T)*TAS2R
      THETA = ((2004.3109D0+(-0.85330D0-0.000217D0*T0)*T0)
     :        +((-0.42665D0-0.000217D0*T0)-0.041833D0*T)*T)*TAS2R

*  Rotation matrix
      CALL slDEUL('ZYZ',-ZETA,THETA,-Z,RMATP)

      END


      SUBROUTINE slDEUL (ORDER, PHI, THETA, PSI, RMAT)
*+
*     - - - - - - -
*      D E U L
*     - - - - - - -
*
*  Form a rotation matrix from the Euler angles - three successive
*  rotations about specified Cartesian axes (double precision)
*
*  Given:
*    ORDER   c*(*)   specifies about which axes the rotations occur
*    PHI     d       1st rotation (radians)
*    THETA   d       2nd rotation (   "   )
*    PSI     d       3rd rotation (   "   )
*
*  Returned:
*    RMAT    d(3,3)  rotation matrix
*
*  A rotation is positive when the reference frame rotates
*  anticlockwise as seen looking towards the origin from the
*  positive region of the specified axis.
*
*  The characters of ORDER define which axes the three successive
*  rotations are about.  A typical value is 'ZXZ', indicating that
*  RMAT is to become the direction cosine matrix corresponding to
*  rotations of the reference frame through PHI radians about the
*  old Z-axis, followed by THETA radians about the resulting X-axis,
*  then PSI radians about the resulting Z-axis.
*
*  The axis names can be any of the following, in any order or
*  combination:  X, Y, Z, uppercase or lowercase, 1, 2, 3.  Normal
*  axis labelling/numbering conventions apply;  the xyz (=123)
*  triad is right-handed.  Thus, the 'ZXZ' example given above
*  could be written 'zxz' or '313' (or even 'ZxZ' or '3xZ').  ORDER
*  is terminated by length or by the first unrecognized character.
*
*  Fewer than three rotations are acceptable, in which case the later
*  angle arguments are ignored.  If all rotations are zero, the
*  identity matrix is produced.
*
*  P.T.Wallace   Starlink   23 May 1997
*
*  Copyright (C) 1997 Rutherford Appleton Laboratory
*  Copyright (C) 1995 Association of Universities for Research in Astronomy Inc.
*-

      IMPLICIT real*8 (a-h,o-z)
C     IMPLICIT NONE

      CHARACTER*(*) ORDER
      DOUBLE PRECISION PHI,THETA,PSI,RMAT(3,3)

      INTEGER J,I,L,N,K
      DOUBLE PRECISION RESULT(3,3),ROTN(3,3),ANGLE,S,C,W,WM(3,3)
      CHARACTER AXIS



*  Initialize result matrix
      DO J=1,3
         DO I=1,3
            IF (I.NE.J) THEN
               RESULT(I,J) = 0D0
            ELSE
               RESULT(I,J) = 1D0
            END IF
         END DO
      END DO

*  Establish length of axis string
      L = LEN(ORDER)

*  Look at each character of axis string until finished
      DO N=1,3
         IF (N.LE.L) THEN

*        Initialize rotation matrix for the current rotation
            DO J=1,3
               DO I=1,3
                  IF (I.NE.J) THEN
                     ROTN(I,J) = 0D0
                  ELSE
                     ROTN(I,J) = 1D0
                  END IF
               END DO
            END DO

*        Pick up the appropriate Euler angle and take sine & cosine
            IF (N.EQ.1) THEN
               ANGLE = PHI
            ELSE IF (N.EQ.2) THEN
               ANGLE = THETA
            ELSE
               ANGLE = PSI
            END IF
            S = DSIN(ANGLE)
            C = DCOS(ANGLE)

*        Identify the axis
            AXIS = ORDER(N:N)
            IF (AXIS.EQ.'X'.OR.
     :          AXIS.EQ.'x'.OR.
     :          AXIS.EQ.'1') THEN

*           Matrix for x-rotation
               ROTN(2,2) = C
               ROTN(2,3) = S
               ROTN(3,2) = -S
               ROTN(3,3) = C

            ELSE IF (AXIS.EQ.'Y'.OR.
     :               AXIS.EQ.'y'.OR.
     :               AXIS.EQ.'2') THEN

*           Matrix for y-rotation
               ROTN(1,1) = C
               ROTN(1,3) = -S
               ROTN(3,1) = S
               ROTN(3,3) = C

            ELSE IF (AXIS.EQ.'Z'.OR.
     :               AXIS.EQ.'z'.OR.
     :               AXIS.EQ.'3') THEN

*           Matrix for z-rotation
               ROTN(1,1) = C
               ROTN(1,2) = S
               ROTN(2,1) = -S
               ROTN(2,2) = C

            ELSE

*           Unrecognized character - fake end of string
               L = 0

            END IF

*        Apply the current rotation (matrix ROTN x matrix RESULT)
            DO I=1,3
               DO J=1,3
                  W = 0D0
                  DO K=1,3
                     W = W+ROTN(I,K)*RESULT(K,J)
                  END DO
                  WM(I,J) = W
               END DO
            END DO
            DO J=1,3
               DO I=1,3
                  RESULT(I,J) = WM(I,J)
               END DO
            END DO

         END IF

      END DO

*  Copy the result
      DO J=1,3
         DO I=1,3
            RMAT(I,J) = RESULT(I,J)
         END DO
      END DO

      END





      SUBROUTINE slDS2C (A, B, V)
*+
*     - - - - - -
*      D S 2 C
*     - - - - - -
*
*  Spherical coordinates to direction cosines (double precision)
*
*  Given:
*     A,B       dp      spherical coordinates in radians
*                        (RA,Dec), (Long,Lat) etc
*
*  Returned:
*     V         dp(3)   x,y,z unit vector
*
*  The spherical coordinates are longitude (+ve anticlockwise
*  looking from the +ve latitude pole) and latitude.  The
*  Cartesian coordinates are right handed, with the x axis
*  at zero longitude and latitude, and the z axis at the
*  +ve latitude pole.
*
*  P.T.Wallace   Starlink   October 1984
*
*  Copyright (C) 1995 Rutherford Appleton Laboratory
*  Copyright (C) 1995 Association of Universities for Research in Astronomy Inc.
*-

      IMPLICIT real*8 (a-h,o-z)
C     IMPLICIT NONE

      DOUBLE PRECISION A,B,V(3)

      DOUBLE PRECISION COSB



      COSB=DCOS(B)

      V(1)=DCOS(A)*COSB
      V(2)=DSIN(A)*COSB
      V(3)=DSIN(B)

      END





      SUBROUTINE slDMXV (DM, VA, VB)
*+
*     - - - - -
*      D M X V
*     - - - - -
*
*  Performs the 3-D forward unitary transformation:
*
*     vector VB = matrix DM * vector VA
*
*  (double precision)
*
*  Given:
*     DM       dp(3,3)    matrix
*     VA       dp(3)      vector
*
*  Returned:
*     VB       dp(3)      result vector
*
*  P.T.Wallace   Starlink   March 1986
*
*  Copyright (C) 1995 Rutherford Appleton Laboratory
*  Copyright (C) 1995 Association of Universities for Research in Astronomy Inc.
*-

      IMPLICIT real*8 (a-h,o-z)
C     IMPLICIT NONE

      DOUBLE PRECISION DM(3,3),VA(3),VB(3)

      INTEGER I,J
      DOUBLE PRECISION W,VW(3)


*  Matrix DM * vector VA -> vector VW
      DO J=1,3
         W=0D0
         DO I=1,3
            W=W+DM(J,I)*VA(I)
         END DO
         VW(J)=W
      END DO

*  Vector VW -> vector VB
      DO J=1,3
         VB(J)=VW(J)
      END DO

      END


      SUBROUTINE slDC2S (V, A, B)
*+
*     - - - - - -
*      D C 2 S
*     - - - - - -
*
*  Direction cosines to spherical coordinates (double precision)
*
*  Given:
*     V     d(3)   x,y,z vector
*
*  Returned:
*     A,B   d      spherical coordinates in radians
*
*  The spherical coordinates are longitude (+ve anticlockwise
*  looking from the +ve latitude pole) and latitude.  The
*  Cartesian coordinates are right handed, with the x axis
*  at zero longitude and latitude, and the z axis at the
*  +ve latitude pole.
*
*  If V is null, zero A and B are returned.
*  At either pole, zero A is returned.
*
*  P.T.Wallace   Starlink   July 1989
*
*  Copyright (C) 1995 Rutherford Appleton Laboratory
*  Copyright (C) 1995 Association of Universities for Research in Astronomy Inc.
*-

      IMPLICIT real*8 (a-h,o-z)
C     IMPLICIT NONE

      DOUBLE PRECISION V(3),A,B

      DOUBLE PRECISION X,Y,Z,R


      X = V(1)
      Y = V(2)
      Z = V(3)
      R = DSQRT(X*X+Y*Y)

      IF (R.EQ.0D0) THEN
         A = 0D0
      ELSE
         A = DATAN2(Y,X)
      END IF

      IF (Z.EQ.0D0) THEN
         B = 0D0
      ELSE
         B = DATAN2(Z,R)
      END IF

      END




      
