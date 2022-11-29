import java.util.Scanner;
import java.lang.Math;


//zad1a
public class Main {
    public static void daodawanie(String[] args){
        int wynik = 0;

        Scanner n = new Scanner(System.in);
        System.out.println("podaj n: ");
        int numer = n.nextInt();

        for (int i = 1; i <= numer;i++){
            System.out.println(("podaj liczbe: "));
            int dodaj = n.nextInt();
            wynik = wynik + dodaj;
        }
        System.out.println("\nSuma wynosi:" + wynik);
    }

//zad1b

   public static void mnozenie(String[] args){
        int wynik = 1;

        Scanner n = new Scanner(System.in);
        System.out.println("podaj n: ");
        int numer = n.nextInt();

        for (int i = 1; i <= numer;i++){
            System.out.println(("podaj liczbe: "));
            int mn = n.nextInt();
            wynik =wynik*mn;
       }
        System.out.println("\nwynik:" + wynik);
    }
//zad1c

    public static void bezw(String[] args) {
         int wynik = 0;
         Scanner n = new Scanner(System.in);
         System.out.println(("podaj n: "));
         int numer = n.nextInt();

         for (int i =1; i<=numer;i++) {
             System.out.println("podaj liczbe: ");
             int bezw = n.nextInt();
             wynik+=Math.abs(bezw);
         }
         System.out.println(("\nWynik: "+ wynik));
         }

    public static void pbezw(String[] args) {
        int wynik = 0;
        Scanner n = new Scanner(System.in);
        System.out.println(("podaj n: "));
        int numer = n.nextInt();

        for (int i =1; i<=numer;i++) {
            System.out.println("podaj liczbe: ");
            int pbezw = n.nextInt();
            wynik+=Math.sqrt(Math.abs(pbezw));
        }
        System.out.println(("\nWynik: "+ wynik));
    }
    public static void mbezw(String[] args) {
        int wynik = 1;
        Scanner n = new Scanner(System.in);
        System.out.println(("podaj n: "));
        int numer = n.nextInt();

        for (int i =1; i<=numer;i++) {
            System.out.println("podaj liczbe: ");
            int bezw = n.nextInt();
            wynik*=Math.abs(bezw);
        }
        System.out.println(("\nWynik: "+ wynik));
    }
    public static void ul(String[] args) {
        int wynik = 0;
        int l2 = 2;
        Scanner n = new Scanner(System.in);
        System.out.println(("podaj n: "));
        int numer = n.nextInt();

        for (int i =1; i<=numer;i++) {
            System.out.println("podaj liczbe: ");
            int pot = n.nextInt();
            wynik+=Math.pow(pot,l2);
        }
        System.out.println(("\nWynik: "+ wynik));
    }
    public static void dm(String[] args) {
        int wynik = 0;
        int mnozenie = 1;
        Scanner n = new Scanner(System.in);
        System.out.println(("podaj n: "));
        int numer = n.nextInt();

        for (int i =1; i<=numer;i++) {
            System.out.println("podaj liczbe: ");
            int liczba = n.nextInt();
            wynik+=liczba;
            mnozenie *=liczba;
        }
        System.out.println(("\nWynikd: " + wynik));
        System.out.println(("\nWynikm: " + mnozenie));
    }
    public static void h(String[] args) {
        int wynik = 1;
        Scanner n = new Scanner(System.in);
        System.out.println(("podaj n: "));
        int numer = n.nextInt();

        for (int i =1; i<=numer;i++) {
            System.out.println("podaj liczbe: ");
            wynik += n.nextInt() * Math.pow((-1),i+1);
        }
        System.out.println(("\nWynik: "+ wynik));
    }
    public static void main(String[] args) {
        int wynik = 0;
        Scanner n = new Scanner(System.in);
        System.out.println(("podaj n: "));
        int numer = n.nextInt();

        for (int i =1; i<=numer;i++) {
            System.out.println("podaj liczbe: ");
            int bezw = n.nextInt();
            wynik+=Math.abs(bezw);
        }
        System.out.println(("\nWynik: "+ wynik));
    }
}
}



