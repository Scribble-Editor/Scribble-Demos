//Breadth First Search algorithm implementation. Created by Patrick M. Howard

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
struct Node;

using List = vector<Node*>;

struct Node
{
    Node();
    Node(char name_)
        : name(name_),
        visited(false),
        previousNode(NULL)
    {
        
    }

    char name;
    bool visited;

    Node* previousNode;

    List children;

    void addChildren(List children_)
    {
        children = children_;
    }
};

void reset(List &list)
{
    for(int i = 0; i < list.size(); ++i)
    {
        list[i]->visited = false;
    }
}


List bfs(Node *startNode, Node *destNode)
{
    List trail;

    queue<Node*> processingQueue;

    processingQueue.push(startNode);
    startNode->visited = true;

    Node* visitedNode = processingQueue.front();

    //Create path
    while(!processingQueue.empty())
    {
        visitedNode = processingQueue.front();    
        processingQueue.pop();

        for(int i = 0; i < visitedNode->children.size(); ++i)
        {
            if(!(visitedNode->children[i]->visited))
            {
                visitedNode->children[i]->visited = true;
                visitedNode->children[i]->previousNode = visitedNode;


                processingQueue.push(visitedNode->children[i]);
            }
        }

        if(visitedNode->name == destNode->name)
        {
            break;
        }

    }

    while(visitedNode != NULL)
    {
        trail.push_back(visitedNode);
        visitedNode = visitedNode->previousNode;
    }

    reverse(trail.begin(), trail.end());

    return trail;
}

int main()
{
    Node nodeA('a');
    Node nodeB('b');
    Node nodeC('c');
    Node nodeD('d');
    Node nodeE('e');
    Node nodeF('f');
    Node nodeG('g');
    Node nodeH('h');

    nodeA.addChildren(List({&nodeB, &nodeC, &nodeD}));
    nodeB.addChildren(List({&nodeE, &nodeD, &nodeC}));
    nodeC.addChildren(List({&nodeH}));
    nodeD.addChildren(List({&nodeE}));
    nodeE.addChildren(List({&nodeF}));
    nodeF.addChildren(List({&nodeG}));
    nodeG.addChildren(List({&nodeH}));
    nodeH.addChildren(List({&nodeA}));

    List nodeList = {&nodeA, &nodeB, &nodeC, &nodeD, &nodeE, &nodeF, &nodeG, &nodeH};

    Node* startNode;
    Node* toNode;

    char inputStart;
    char inputDest;

    while(1)
    {
        reset(nodeList);

        cout << "From what node? ";
        cin >> inputStart;

        cout << "To what node? ";
        cin >> inputDest;

        for(int i = 0; i < nodeList.size(); ++i)
        {
            if(inputStart == nodeList[i]->name)
            {
                startNode = nodeList[i];
            }

            if(inputDest == nodeList[i]->name)
            {
                toNode = nodeList[i];
                break;
            }
        }
        
        if(startNode != nullptr && toNode != nullptr)
        {
            List trail = bfs(startNode, toNode);
            for(int i = 0; i < trail.size(); ++i)
            {
                cout << trail[i]->name << " ";
            }

            cout << "\nTrail size: " << trail.size() << "\n";
        }
        else
        {
            cout << "Not sure what those nodes are, try again.\n";
        }
    }

}