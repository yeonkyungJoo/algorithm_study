package leegijin;

import java.util.Arrays;

public class p_쿼드압축후개수세기 {
    public static void main(String[] args) {
        int[][] arr = {{1,1,0,0},{1,0,0,0},{1,0,0,1},{1,1,1,1}};

        int []answer = solution(arr);
        for(int t: answer){
            System.out.println("t = " + t);
        }
    }

    static int zeroCnt = 0, oneCnt = 0;
    static double[] dx = {0, 0, 0.5, 0.5};
    static double[] dy = {0, 0.5, 0, 0.5};
    static int[][] copyArr;

    public static int[] solution(int[][] arr) {
        int[] answer = new int[2];
        copyArr = arr;

        if(!isCompression(arr.length, 0,0))
            compression(0,0, arr.length);
        answer[0] = zeroCnt;
        answer[1] = oneCnt;

        return answer;
    }

    public static void compression(int x, int y, int size) {

        for(int i=0; i<4; i++) {
            int nx = x + (int) (size * dx[i]);
            int ny = y + (int) (size * dy[i]);

            if( !isCompression(size/2, nx, ny) )
                compression(nx, ny, size/2);

        }
    }

    public static boolean isCompression(int size, int x, int y) {
        int num = copyArr[x][y];

        for(int i=x; i<x+size; i++) {
            for(int j= y; j<y+size; j++) {
                if(num != copyArr[i][j])
                    return false;
            }
        }

        if(num == 0) zeroCnt++;
        else oneCnt++;

        return true;
    }
}