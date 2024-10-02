import java.util.Scanner;
class test2{
    public static void main(String[] args) {
        Scanner a= new Scanner(System.in);
        int n= a.nextInt();
        int i =0;
        int first=0;
        int second =1;
        while(i<n){
            System.out.print(first+" ");
            int next=first+second;
            first=second;
            second=next;
            i++;
        }
        a.close();
    }
}