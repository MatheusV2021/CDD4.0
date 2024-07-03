package array;

import java.util.Arrays;

public class exercicio_array03 {
	public static void main(String[] args) {
		
		int a[] = {81, 32, 17, 8, 20, 91, 43};
		int b[] = new int[a.length];
		
		System.out.print("Array A: ");
		
		for (int z = 0; z<7; z++) {
			System.out.print(a[z]+" ");
		}
		
		//1° Imprimir invertido
		
		System.out.println(" ");
		System.out.print("Array A invertido: ");
		
		for (int i = 6; i>=0; i--) {
			System.out.print(a[i]+" ");
		}
		
		
		
		//2° Guardar em outro array
		
		for (int t = a.length - 1; t >= 0; t--) {
		    b[b.length - t - 1] = a[t];
		}
		
		System.out.println(" ");
		System.out.print("Array B: ");
		
		for (int y = 0; y<7; y++) {
			System.out.print(b[y]+" ");
		}
		
		
		
		//3° Imprimir ordenado em forma crescente
		
		Arrays.sort(a);
		System.out.println(" ");
        System.out.print("Array A em ordem crescente: ");
        for (int num : a) {
            System.out.print(num + " ");
        }
	}
}
