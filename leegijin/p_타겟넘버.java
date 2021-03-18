package leegijin;

import java.util.LinkedList;
import java.util.Queue;

public class p_타겟넘버 {
    public static class TWO{
        int x;
        int y;

        public TWO(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) {
        int [] numbers= {1, 1, 1, 1, 1};
        int target = 3;
        System.out.println(solution(numbers,target));
    }
    static int answer;
    public static int solution(int[] numbers, int target) {
       // dfs(numbers,0,numbers[0],target);
       // dfs(numbers,0,-numbers[0],target);
        bfs(numbers,target);
        return answer;
    }
    public static void dfs(int [] numbers, int i ,int sum,int target){
        //종료구문
        if(i==numbers.length-1 && sum!=target)
            return;
        else if(i==numbers.length-1 && sum==target) {

            answer = answer + 1;
        }
        else{
            i=i+1;
            dfs(numbers, i, sum - numbers[i],target);
            dfs(numbers, i, sum + numbers[i],target);

        }
    }
    public static void bfs(int[] numbers, int target){
        Queue<TWO> queue = new LinkedList<TWO>();
        queue.add(new TWO(numbers[0],0));
        queue.add(new TWO(-numbers[0],0));
        int i=1;
        while(!queue.isEmpty()){
            TWO t = queue.poll();
            int tmp=t.x;
            int cnt=t.y;
            if(cnt==numbers.length-1&&tmp==target)
                answer=answer+1;
            else if(cnt==numbers.length-1&&tmp!=target)
                continue;
            else {
                cnt=cnt+1;
                queue.offer(new TWO(tmp+numbers[cnt],cnt));
                queue.offer(new TWO(tmp-numbers[cnt],cnt));
            }
        }
    }
}
