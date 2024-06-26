package basico1;

import java.util.Scanner;

public class exercicio5 {
	public static void main(String[] args) {
		
		int num, num2, media;
		
		Scanner entrada = new Scanner(System.in);
		System.out.print("Insira sua nota 1: ");
		num = entrada.nextInt();
		
		Scanner entrada2 = new Scanner(System.in);
		System.out.print("Insira sua nota 2: ");
		num2 = entrada2.nextInt();
		
		media = (num+num2)/2;
		
		System.out.println(media);
		
	}

}
