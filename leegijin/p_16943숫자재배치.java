package leegijin;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p_16943숫자재배치 {
    //두 정수 A와 B가 있을 때, A에 포함된 숫자의 순서를 섞어서 새로운 수 C를 만들려고 한다. 즉, C는 A의 순열 중 하나가 되어야 한다.
    //
    //가능한 C 중에서 B보다 작으면서, 가장 큰 값을 구해보자. C는 0으로 시작하면 안 된다.

    static int cnt =0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine()," ");
        String A = s.nextToken();
        int B = Integer.parseInt(s.nextToken());
        boolean[] visit = new boolean[A.length()];
        dfs(A,B,"",visit);
        if(cnt==0)
            cnt=-1;
        System.out.println(cnt);
    }
    static void dfs(String A, int B, String current, boolean[] visit){
        if(current.length()==A.length()&&current.charAt(0)!='0') {
            if(Integer.parseInt(current) < B)
                cnt = Math.max(cnt,Integer.parseInt(current));
        }
        for(int i =0 ; i< A.length() ; i++){
            if(!visit[i]) {
                visit[i]=true;
                dfs(A, B, current + A.charAt(i), visit);
                visit[i]=false;
            }
        }
    }
}
