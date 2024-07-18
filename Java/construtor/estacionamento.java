package construtor;

public class estacionamento {
	public static void main(String[] args) {
		Carro c1 = new Carro();
		c1.cor = "Azul";
		c1.preco = 3000;
		c1.modelo = "Fiat Uno";
		Carro c2 = new Carro();
		c2.cor = "Preto";
		c2.preco = 1000;
		c2.modelo = "Fiat Marea";
		
		System.out.printf("Carro 01\n \n"+"Modelo: "+c1.modelo+"\n"+"Cor: "+c1.cor+"\n"+"Preço: "+c1.preco);
		System.out.printf("\n \nCarro 02\n \n"+"Modelo: "+c2.modelo+"\n"+"Cor: "+c2.cor+"\n"+"Preço: "+c2.preco);
		
		

	}
}
