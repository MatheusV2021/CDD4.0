package ÉOFIM;


public class Triatleta implements Atleta, Ciclista, Corredor, Nadador{
	public boolean nadando = false;
	public boolean correndo = false;
	public boolean pedalando = false;
	public boolean descansando = false;
	
	
	public void nadar() {
		if (descansando) {
            nadando = true;
            descansando = false;
            System.out.println("Você está nadando...");
        } 
		
		else if(nadando) {
			System.out.println("Você já está nadando...");
		}
		
		else {
            System.out.println("Descanse primeiro.");
        }
	}

	
	public void correr() {
		if (descansando) {
            correndo = true;
            descansando = false;
            System.out.println("Você está correndo...");
        } 
		
		else if(correndo) {
			System.out.println("Você já está correndo...");
		}
		
		else {
            System.out.println("Descanse primeiro.");
        }
	}

	
	public void pedalar() {
		if (descansando) {
            pedalando = true;
            descansando = false;
            System.out.println("Você está pedalando...");
        } 
		
		else if(pedalando) {
			System.out.println("Você já está pedalando...");
		}
		
		else {
            System.out.println("Descanse primeiro.");
        }
	}

	
	public void descansar() {
		if (nadando || correndo || pedalando || !descansando) {
            descansando = true;
            System.out.println("Você está descansando...");
        } else {
            System.out.println("Já está descansando.");
        }
	}
	
	
}	
