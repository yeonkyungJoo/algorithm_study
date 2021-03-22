package leegijin;

public class p_카펫 {
    public static void main(String[] args) {
        int brown =10;
        int yellow =2;
        int [] arr =solution(brown,yellow);
        System.out.println(arr[0]+","+arr[1]);
    }
    public static int[] solution(int brown, int yellow) {
        int[] answer = new int [2];
        // brown+yellow =answer[1]*answer[2];
        // (answer[1]-2)*(answer[2]-2)=yellow
        // answer[1]*answer[2] -2(answer[1]+answer[2])+4 =yellow
        // brown+yellow -2(answer[1]+answer[2])=yellow
        // brown = 2(answer[1]+answer[2]-2)
        int a = brown/2;
        System.out.println(a);
        int tmp = 0;
        for(int i=2; i< a; i++){
            if((i-2)*(a-i)==yellow){
                tmp=i;
                break;
            }
        }
        answer[0]=a-tmp+2;
        answer[1]=tmp;
        return answer;
    }
}
