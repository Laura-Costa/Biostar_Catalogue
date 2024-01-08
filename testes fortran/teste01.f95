! Todo programa Fortran tem três seções
! Seção de Declaração
! Seção de Execução
! Seção de Terminação
PROGRAM teste01
	IMPLICIT NONE
	! Seção de declaração
	INTEGER :: i ! variável do tipo inteiro
	INTEGER :: valor
	i = 999
	! o ; serve para separar instruções
	50 valor = 10
	valor = valor * 5; valor = valor * 10
	! aqui são escritas as instruções
	! & é o marcador de continuação de linha
	! Seção de Execução
	!valor = 2 + 3 - 5 / 6 &
	!& -1 * 10
	WRITE(*,*) 'Valor de valor: ', valor
END PROGRAM teste01
