class Solution {
public:
    struct permute{
        vector<string> array;
        string cur;
        int idx;
    };
    void dfs(permute tmp){
        for(int i=tmp.idx;i<tmp.array.size();i++){
            string s = tmp.cur+tmp.array[i];
            bool flag=true;
            for(int j=0;j<s.length();j++){
                if(count(s.begin(),s.end(),s[j])>1){
                    flag=false;
                    break;
                }
            }
            if(flag){
                permute next = tmp;
                next.cur+=next.array[i];
                if(next.cur.length()>ans){
                    ans = next.cur.length();
                }
                next.idx = i+1;
                dfs(next);
            }
        }
    }
    int maxLength(vector<string>& arr) {
        permute tmp{arr,"",0};
        dfs(tmp);
        return ans;
    }
private:
    int ans = 0;
};