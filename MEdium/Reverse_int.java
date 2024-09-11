class Solution {
    public int reverse(int x) {
        try{
            double result = 0;
            if(x<=Integer.MIN_VALUE || x>=Integer.MAX_VALUE){
                return 0;
            }
            if(x > 0){
                while(x !=0){
                    int rem = x % 10;
                    x = (int) x / 10;
                    result = result*10 + rem;
                }
                if((int)result >= Integer.MAX_VALUE){
                    return 0;
                }
                return (int)result;
            }
            else if (x<0){
                x = x*-1;
                while(x !=0){
                    int rem = x % 10;
                    x = (int) x / 10;
                    result = result*10 + rem;
                }
                int result1 = (int)(result*-1);
                if(result1  > Integer.MIN_VALUE){
                    return result1;
                }else if(result1  <= Integer.MIN_VALUE){
                    return 0;
                }
                else{
                    return 0;
                }
                
            }
        }catch(Exception e){
            return 0;
        }
        return 0;
    }
}
