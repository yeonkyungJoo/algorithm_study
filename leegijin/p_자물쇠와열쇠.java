import java.util.*;

public class p_자물쇠와열쇠 {
    public static void main(String[] args) {
        int [][] key = {{0, 0, 0},{1, 0, 0},{0, 1, 1}};
        int [][] lock ={{1, 1, 1},{1, 1, 0},{1, 0, 1}};
        if(solution(key,lock)){
            System.out.println(true);
        }
        else
            System.out.println(false);
    }
    public static boolean solution(int[][] key, int[][] lock) {
        int size = lock.length - 1;

        for(int d = 0 ; d < 4 ; ++d) {
            int[][] rotatedKey = rotate(d, key);
            int[][] paddedKey = padding(rotatedKey, size);

            for(int R = 0 ; R < paddedKey.length - size ; ++R) {
                for(int C = 0 ; C < paddedKey[0].length - size ; ++C) {
                    boolean flag = true;

                    for(int r = 0 ; r < lock.length ; ++r) {
                        for(int c = 0 ; c < lock[0].length ; ++c) {
                            if(lock[r][c] == paddedKey[R + r][C + c]) flag = false;
                        }
                    }

                    if(flag) return true;
                }
            }
        }

        return false;
    }

    private static int[][] padding(int[][] arr, int size) {
        int[][] result = new int[arr.length + size * 2][arr[0].length + size * 2];

        for(int r = 0 ; r < arr.length ; ++r) {
            for(int c = 0 ; c < arr[0].length ; ++c) {
                result[r + size][c + size] = arr[r][c];
            }
        }

        return result;
    }

    private static int[][] rotate(int cnt, int[][] arr){
        if(cnt == 0) return arr;

        int[][] result = null;
        int[][] origin = copy(arr);

        for(int i = 0 ; i < cnt ; ++i) {
            result = new int[arr.length][arr[0].length];

            for(int r = 0 ; r < origin.length ; ++r) {
                for(int c = 0 ; c < origin[0].length ; ++c) {
                    result[c][origin.length - 1 - r] = origin[r][c];
                }

            }
            origin = result;
        }

        return result;
    }

    private static int[][] copy(int[][] arr){
        int[][] result = new int[arr.length][arr[0].length];

        for(int r = 0 ; r < arr.length ; ++r) {
            for(int c = 0 ; c < arr[r].length ; ++c) {
                result[r][c] = arr[r][c];
            }
        }

        return result;
    }
}