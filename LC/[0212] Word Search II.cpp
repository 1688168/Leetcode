class Solution {
    class TrieNode
    {
        public:
        TrieNode* next[26];
        bool isEnd;
        int count = 0;
        TrieNode()
        {
            for (int i=0; i<26; i++)
                next[i]=NULL;
            isEnd=false;
            count=0;
        }
    };
    TrieNode* root;
    vector<string>rets;
    int M, N;
    bool visited[12][12];
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words)
    {
        M=board.size();
        N=board[0].size();
        root=new TrieNode();
        for (int i=0; i<words.size(); i++)
        {
            TrieNode* node=root;
            for (auto ch: words[i])
            {
                if (node->next[ch-'a']==NULL)
                    node->next[ch-'a']=new TrieNode();
                node=node->next[ch-'a'];
                node->count++;
            }
            node->isEnd=true;
        }

        for (int i=0; i<M; i++)
         for (int j=0; j<N; j++)
         {
             TrieNode* node = root;
             string word;
             visited[i][j]=1;
             DFS(i,j,node,word,board);
             visited[i][j]=0;
         }

        return rets;
    }

    void DFS(int i, int j, TrieNode* node, string& word, vector<vector<char>>& board)
    {
        if (node->next[board[i][j]-'a']==NULL) return;
        if (node->next[board[i][j]-'a']->count==0) return;

        node = node->next[board[i][j]-'a'];
        word.push_back(board[i][j]);

        if (node->isEnd==true)
        {
            node->isEnd = false;
            rets.push_back(word);
            remove(root, word);
        }

        vector<pair<int,int>>dir={{1,0},{-1,0},{0,1},{0,-1}};

        for (int k=0; k<4; k++)
        {
            int x=i+dir[k].first;
            int y=j+dir[k].second;
            if (x<0||x>=M||y<0||y>=N) continue;
            if (visited[x][y]==1) continue;

            visited[x][y]=1;
            DFS(x,y,node,word,board);
            visited[x][y]=0;
        }

        word.pop_back();
    }

    void remove(TrieNode* root, string word)
    {
        TrieNode* node = root;
        for (auto ch: word)
        {
            node = node->next[ch-'a'];
            node->count --;
        }
    }
};
