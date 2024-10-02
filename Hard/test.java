import java.util.Scanner;
class test{
    public static int fib(int n){
        if(n==0){
            return 0;
        }else if(n==1 || n==2){
            return 1;
        }else{
            return fib(n-1)+fib(n-2);
        }
    }
    public static void main(String[] args) {
        Scanner a= new Scanner(System.in);
        int n= a.nextInt();
        int i =0;
        while(i<n){
            System.out.println(fib(i)+" ");
            i++;
        }
        a.close();
    }
}