package repeticoes2;

import java.util.Scanner;

public class exercicio5 {
	public static void main(String[] args) {
		double num, soma, nota, media;
		soma = 0;
		
		Scanner entrada = new Scanner(System.in);
		System.out.println("Numero de alunos: ");
		num = entrada.nextInt();
		
		for (int x = 0; x<num;x++) {
			System.out.println("Insira sua nota: ");
			nota = entrada.nextInt();
			soma += nota;
			
		}
		
		media = soma/num;
		
		System.out.println(media);
		
		entrada.close();
	}
}
