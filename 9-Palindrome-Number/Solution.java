class Solution {
    public boolean isPalindrome(int x) {
        String y = String.valueOf(x);
        int size = y.length() - 1;

        for(int i = 0; i < size; i++){
            if(y.charAt(i) == y.charAt(size - i)){
                continue;
            }else{
                return false;
            }
        }
        return true;
    }
}