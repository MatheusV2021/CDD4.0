package basico1;
import java.util.Scanner;


public class exercicio03 {
	public static void main(String[] args) {
		double resp, resp2, resp3;
		
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		resp = entrada.nextDouble();
		
		Scanner entrada2 = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		resp2 = entrada.nextDouble();
		
		Scanner entrada3 = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		resp3 = entrada.nextDouble();
		
		if(resp > resp2 && resp > resp3) {
			System.out.println(resp+" é maior");
		}
		
		else if(resp2 > resp && resp2 > resp3) {
			System.out.println(resp2+" é maior");
		}
		
		else {
			System.out.println(resp3+" é maior");
		}
	}
}
