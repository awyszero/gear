/*
* this is simple program to ask the user to enter one word and then check if the word is palindrome
*  palindrome is mean that word can be reads the same backword or forward
*
*
* */


import java.util.Scanner;
public class gear4 {

    public static void main(String[] args)
    {
        gear4 o = new gear4();
        o.solve();
    }

    public String input()
    {
        System.out.println("plaese enter word:>");
        Scanner s = new Scanner(System.in);
        String text =s.next();
        return text;

    }

    public void solve ()
    {
        String reverase="";
        String a = input();
        a =a.toLowerCase();
        for (int x =a.length()-1;x>=0;x--)
        {
            reverase =reverase + a.charAt(x);
        }
        if (a.equals(reverase))
        {
            System.out.println("this word is palindrome");
        }
        else
        {
            System.out.println("this word is not palindrome");
        }
    }
}
