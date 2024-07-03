package array;

import java.util.Scanner;

public class exercicio_array02 {
	public static void main(String[] args) {
		int notas[] = new int[5];
		int soma = 0;
		Scanner entrada = new Scanner(System.in);
		
		for (int x = 0; x<notas.length; x++) {
			System.out.print("Insira sua nota: ");
			notas[x] = entrada.nextInt();
		}
		
		for (int i:notas) {
			soma += i;
		}
		
		int media = soma/5;
		System.out.print(media);
		
		entrada.close();
	}

}
