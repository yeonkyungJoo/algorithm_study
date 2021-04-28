package leegijin;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class p_16936나3곱2 {
    static String answ;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer s = new StringTokenizer(br.readLine()," ");
        ArrayList<Long> arr = new ArrayList<>();
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0; i<n ; i++){
            arr.add(Long.parseLong(s.nextToken()));
        }
        boolean [] visit = new boolean[n];
        for(int i=0 ; i<arr.size() ;i++){
            if(!visit[i]) {
                visit[i]=true;
                dfs(arr, arr.get(i), visit,0,String.valueOf(arr.get(i)));
                visit[i]=false;
            }
        }
        System.out.println(answ);
    }
    static void dfs(ArrayList<Long> arr, long current, boolean[] visit,int cnt,String ans) {
        if(cnt==arr.size()-1)
        {
            answ =ans;
        }
        if(arr.contains(current)){
            int tmp = arr.indexOf(current*2);
            if(tmp>=0&&!visit[tmp]) {
                visit[tmp]=true;
                dfs(arr, current * 2, visit,cnt+1,ans+" "+String.valueOf(current*2));
                visit[tmp]=false;
            }
            if(current%3==0) {
                tmp = arr.indexOf(current / 3);
                if (tmp >= 0 && !visit[tmp]) {
                    visit[tmp] = true;
                    dfs(arr, current / 3, visit, cnt + 1, ans+" "+String.valueOf(current/3));
                    visit[tmp]= false;
                }
            }
        }
    }
}
