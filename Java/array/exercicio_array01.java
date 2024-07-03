package array;

import java.util.Scanner;

public class exercicio_array01 {
	public static void main(String[] args) {
		int a[] = new int [10];
		int b[] = new int [10];
		int c[] = new int [10];
		int d[] = new int [10]; 
		Scanner entrada = new Scanner(System.in);
		
		for (int x = 0; x<a.length; x++) {
			System.out.print("Insira um numero na posição "+x+" do array: ");
			a[x] = entrada.nextInt();
		}
		
		for (int y = 0; y<a.length; y++) {
			System.out.print("Insira um numero na posição "+y+" do array: ");
			b[y] = entrada.nextInt();
		}
		
		for (int z = 0; z<a.length; z++) {
			System.out.print("Insira um numero na posição "+z+" do array: ");
			c[z] = entrada.nextInt();
		}
		
		for (int w = 0; w<a.length; w++) {
			System.out.print("Insira um numero na posição "+w+" do array: ");
			d[w] = entrada.nextInt();
		}
		
		for (int i : a) {
			System.out.print(a+" ");
		}
		
		for (int i : b) {
			System.out.print(b+" ");
		}
		
		for (int i : c) {
			System.out.print(c+" ");
		}
		
		for (int i : d) {
			System.out.print(d+" ");
		}
	}

}
