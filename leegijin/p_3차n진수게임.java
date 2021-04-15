package leegijin;

public class p_3차n진수게임 {
    public static void main(String[] args) {
        String tmp = solution(2,4,2,1);
        System.out.println("tmp = " + tmp);
        tmp = solution(16,16,2,1);
        System.out.println("tmp = " + tmp);
        tmp = solution(16,16,2,2);
        System.out.println("tmp = " + tmp);
    }
    public static String solution(int n, int t, int m, int p) {
        String sl ="";
        String answer ="";
        for(int i=0; i<=m*t; i++) {
            sl = sl+nchange(n,i);
        }
        for(int i=p-1; i<sl.length(); i=i+m){
            if(answer.length()==t)
                break;;
            answer=answer+sl.charAt(i);
        }
        return answer;
    }
    public static String nchange(int n, int num){
        String s = "";
        if(num==0)
            return "0";
        while(num>0) {
            if (num % n == 0)
                s = "0"+s ;
            else {
                s = Integer.toHexString(num % n) + s;
            }
            num=num/n;
        }
        return s.toUpperCase();
    }
}
