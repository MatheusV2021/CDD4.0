package basico1;

import java.util.Scanner;


public class exercicio02 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		double resp = entrada.nextDouble();
		
		if(resp % 2 == 0) {
			System.out.println(resp+"é par");
		}
		else {
			System.out.println(resp+"é impar");
		}
			
	}

}
