package leegijin;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class p_16938캠프준비 {
    static int cnt =0;
    public static void main(String[] args) throws IOException {
    //*백준이는 문제를 N개 가지고 있고, 모든 문제의 난이도를 정수로 수치화했다. i번째 문제의 난이도는 Ai이다.
        //
        //캠프에 사용할 문제는 두 문제 이상이어야 한다. 문제가 너무 어려우면 학생들이 멘붕에 빠지고, 문제가 너무 쉬우면 학생들이 실망에 빠지게 된다. 따라서, 문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야 한다. 또, 다양한 문제를 경험해보기 위해 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 한다.
        //
        //캠프에 사용할 문제를 고르는 방법의 수를 구해보자.
        // N, L, R, X
        int N = 0;
        int L = 0;
        int R = 0;
        int X = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine()," ");
        for(int i=0; i<s.countTokens() ; i++){
            N = Integer.parseInt(s.nextToken());
            L = Integer.parseInt(s.nextToken());
            R = Integer.parseInt(s.nextToken());
            X = Integer.parseInt(s.nextToken());
        }
        int [] arr= new int[N];
        s= new StringTokenizer(br.readLine()," ");
        for(int i=0; i<N ; i++){
            arr[i]=Integer.parseInt(s.nextToken());
        }
        boolean visit[] =new boolean[N];
        ArrayList<Integer>cl =new ArrayList<>();
        dfs(arr,L,R,X,visit,0,cl);
        System.out.println(cnt);

    }
    static void dfs(int[] arr, int L, int R, int X, boolean[] visit, int start, ArrayList<Integer> cl){
        if(cl.size()>=2) {
            int min =123456789;
            int max =0;
            int sum =0;
            for(int tmp: cl){
                sum=sum+tmp;
                min = Math.min(min,tmp);
                max = Math.max(max,tmp);
            }
            if(sum>=L && sum<=R &&max-min>=X)
                cnt++;
        }
        for(int i=start ; i<arr.length ; i++){
            if(!visit[i]) {
                visit[i] = true;
                cl.add(arr[i]);
                dfs(arr, L, R, X, visit, i ,cl);
                cl.remove(cl.size()-1);
                visit[i] = false;
            }
        }
    }
}
