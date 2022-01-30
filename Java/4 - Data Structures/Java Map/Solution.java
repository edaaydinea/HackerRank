//Complete this code or write your own from scratch
import java.awt.image.ImageProducer;
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh)
    {
        Map<String,Integer> name_phone = new HashMap<>();
        Scanner in = new Scanner(System.in);
        int n=in.nextInt();
        in.nextLine();
        for(int i=0;i<n;i++)
        {
            String name=in.nextLine();
            int phone=in.nextInt();
            name_phone.put(name,phone);
            in.nextLine();
        }
        while(in.hasNext())
        {
            String s=in.nextLine();
            if (name_phone.containsKey(s))
                System.out.println(s + "="+ name_phone.get(s));
            else
                System.out.println("Not found");
        }
    }
}



