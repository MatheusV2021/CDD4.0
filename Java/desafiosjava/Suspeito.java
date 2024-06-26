import java.util.Scanner;

public class Main {
  public static void main(String[] args) {

    int suspeito = 0;
    int p1, p2, p3, p4, p5;

    Scanner entrada = new Scanner(System.in);
    System.out.println("Telefonou para a vítima? [1]- Sim [2]- Não");
    p1 = entrada.nextInt();

    if (p1 == 1) {
      ++suspeito;
    }

    Scanner entrada2 = new Scanner(System.in);
    System.out.println("Esteve no local do crime? [1]- Sim [2]- Não");
    p2 = entrada2.nextInt();

    if (p2 == 1) {
      ++suspeito;
    }

    Scanner entrada3 = new Scanner(System.in);
    System.out.println("Mora perto da vítima? [1]- Sim [2]- Não");
    p3 = entrada3.nextInt();

    if (p3 == 1) {
      ++suspeito;
    }

    Scanner entrada4 = new Scanner(System.in);
    System.out.println("Devia para a vítima? [1]- Sim [2]- Não");
    p4 = entrada4.nextInt();

    if (p4 == 1) {
      ++suspeito;
    }

    Scanner entrada5 = new Scanner(System.in);
    System.out.println("Já trabalhou com a vítima? [1]- Sim [2]- Não");
    p5 = entrada5.nextInt();

    if (p5 == 1) {
      ++suspeito;
    }
      

    if (suspeito == 2) {
      System.out.println("Suspeito");
    }

    else if (suspeito == 3 || suspeito == 4) {
      System.out.println("Cúmplice");
    }

    else if (suspeito == 5) {
      System.out.println("Assassino");
    }

    else {
      System.out.println("Inocente");
    }

    entrada.close();
    entrada2.close();
    entrada3.close();
    entrada4.close();
    entrada5.close();
    
  }

  
}
