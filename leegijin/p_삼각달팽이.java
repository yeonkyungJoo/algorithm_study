package leegijin;

public class p_삼각달팽이 {
    public static void main(String[] args) {
        int n =4;
        int[] tmp = solution(n);
        for(int t: tmp){
            System.out.println("t = " + t);
        }
    }
    public static int[] solution(int n) {

        int[] answer = new int[n*(n+1)/2];

        int[][] arr = new int[n][n];
        int count = 1;
        int row = -1;
        int col = 0;
        int answerIndex = 0;

        while(true) {
            for(int i=0; i<n; i++) {
                row += 1;
                arr[row][col] = count;
                count ++;
            }
            n --;
            if(n == 0) {
                break;
            }

            for(int i=0; i<n; i++) {
                col += 1;
                arr[row][col] = count;
                count ++;
            }
            n --;
            if(n == 0) {
                break;
            }

            for(int i=0; i<n; i++) {
                row -= 1;
                col -= 1;
                arr[row][col] = count;
                count ++;
            }
            n --;
            if(n == 0) {
                break;
            }
        }

        for(int i=0; i<arr.length; i++) {
            for(int j=0; j<arr[i].length; j++) {
                if(arr[i][j] == 0) {
                    break;
                }
                answer[answerIndex] = arr[i][j];
                answerIndex ++;
            }
        }
        return answer;
    }

}
