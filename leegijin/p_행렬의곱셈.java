package leegijin;

public class p_행렬의곱셈 {
    public static void main(String[] args) {
        int[][] arr1 ={{2, 3, 2},{4, 2, 4},{3, 1, 4}};
        int[][] arr2={{5, 4, 3},{2, 4, 1},{3, 1, 1}};
        int[][] tmp = solution(arr1,arr2);
        for(int[] t : tmp){
            System.out.print("[");
            for (int i : t){
                System.out.print(i+" ");
            }
            System.out.println("]");
        }
    }
    public static int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] result = new int[arr1.length][arr2[0].length];
        for(int i=0;i<result.length;i++){
            for(int j=0;j<result[0].length;j++){
                int temp = 0;
                for(int k=0;k<arr1[0].length;k++){
                    temp+=arr1[i][k]*arr2[k][j];
                }
                result[i][j] = temp;
            }
        }
        return result;
    }
}
