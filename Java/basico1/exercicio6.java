package basico1;

import java.util.Scanner;

public class exercicio6 {
	public static void main(String[] args) {
		char esc;
		
		Scanner entrada = new Scanner(System.in);
		System.out.println("Selecione: [M] - Masculino [F]-Feminino");
		esc = entrada.next().charAt(0);
		
		if(esc == 'M') {
			System.out.println("Masculino");
		}
		else if(esc == 'F') {
			System.out.println("Feminino");
		}
		else{
			System.out.println("Invalido");
		}
	}
}
