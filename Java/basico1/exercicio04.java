package basico1;

import java.util.Scanner;

public class exercicio04 {
	public static void main(String[] args) {
		int num;
		
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		num = entrada.nextInt();
		
		if(num == 1) {
			System.out.println("Domingo");
		}
		else if(num == 2) {
			System.out.println("Segunda-feira");
		}
		else if(num == 3) {
			System.out.println("Terça-feira");
		}
		else if(num == 4) {
			System.out.println("Quarta-feira");
		}
		else if(num == 5) {
			System.out.println("Quinta-feira");
		}
		else if(num == 6) {
			System.out.println("Sexta-feira");
		}
		else if(num == 7) {
			System.out.println("Sabado");
		}
		else {
			System.out.println("Valor invalido");
		}
		
		entrada.close();
	}

}
