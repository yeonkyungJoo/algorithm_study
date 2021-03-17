package leegijin;

public class p_주식가격 {
    public static void main(String[] args) {
        int [] prices = {1, 2, 3, 2, 3};
        for(int tmp : solution(prices)){
            System.out.println("tmp = " + tmp);
        }
    }
    public static int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        for(int i=0; i<prices.length;i++){ // i 지점부터 스타트
            int cnt =0;
            for(int j=i+1; j<prices.length; j++){
                if(prices[i]>prices[j]){
                    cnt++;
                    break;
                }
                cnt++;
            }
            answer[i]=cnt;
        }
        return answer;
    }
}
