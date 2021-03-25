package leegijin;

public class p_다음큰숫자 {
    public static void main(String[] args) {
        int n= 78; //1001110  15      //83 1010011  23
        System.out.println(solution(n));
    }
    public static int convert(int n){
        String tmp = Integer.toString(n,2);
        int cnt = 0;
        for(int i=0;i<tmp.length();i++){
            if(tmp.charAt(i)=='1') cnt++;
        }
        return cnt;
    }
    public static int solution(int n){
        String binN = Integer.toString(n,2);
        int cnt = 0;
        for(int i=0;i<binN.length();i++){
            if(binN.charAt(i)=='1') cnt++;
        }
        int current = n+1;
        while(true){
            if(convert(current)==cnt) return current;
            current++;
        }
    }
}
