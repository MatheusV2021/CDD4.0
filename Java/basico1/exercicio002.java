package basico1;

import java.util.Scanner;


public class exercicio002 {
	public static void main(String[] args) {
		int resp;
		
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		resp = entrada.nextInt();
		
		if(resp > 0) {
			System.out.println(resp+" é positivo");
		}
		
		else if(resp == 0) {
			System.out.println(resp+" é zero");
		}
		
		else {
			System.out.println(resp+" é negativo");
		}
	}

}
