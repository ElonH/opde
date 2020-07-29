#include <iostream>
#include <list>
#include <nlohmann/json.hpp>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

using json = nlohmann::json;
using string = std::string;
template <class T>
using list = std::list<T>;
template <class T>
using vector = std::vector<T>;
template <class T>
using unordered_set = std::unordered_set<T>;

struct deps_node
{
    size_t id;
    string name;
    int cost, total_cost;
    list<deps_node *> in_nodes, out_nodes;
    bool inited = false;

    deps_node() : id(0), name(""), cost(0), total_cost(-1), in_nodes(), out_nodes() {}
};

class DependsTree
{
    deps_node nodes_pool[10000 * 3] = {};

public:
    size_t max_id = 0;
    void AddNode(const size_t &id, const string &name, const int cost)
    {
        auto &node = this->nodes_pool[id];
        node.id = id;
        max_id = std::max(max_id, id);
        node.cost = cost;
        node.name = name;
        node.inited = true;
    }

    void AddEdge(size_t from, size_t to)
    {
        auto src = &this->nodes_pool[from];
        auto dst = &this->nodes_pool[to];
        src->out_nodes.push_back(dst);
        dst->in_nodes.push_back(src);
    }

    vector<deps_node *> root_nodes;

    /**
     * @brief top node: in degree = 0
     * bottom node: out degree = 0
     */
    void ExtractRootNodes()
    {
        root_nodes.clear();
        for (auto &&i : nodes_pool)
        {
            if (i.inited && i.in_nodes.size() == 0)
                root_nodes.push_back(&i);
        }
    }

    deps_node *GetNodeById(size_t id)
    {
        return &nodes_pool[id];
    }
};

/**
 * @brief Orthogonal linked 2-d matrix
 *
 */
template <class Tdata>
struct OlMatrix
{
public:
    struct Node
    {
        Tdata data;
        Node *m_row_pre = nullptr, *m_row_next = nullptr, *m_col_pre = nullptr, *m_col_next = nullptr;
    };
    list<Node *> m_row_heads, m_col_heads;

protected:
    Node *m_node_pool = nullptr;
    size_t m_allocated_cnt = 0;

public:
    Node origin;
    /**
     * @brief Construct a new Ol Matrix object
     *
     * @param rows rows number of matrix
     * @param cols columns number of matrix
     */
    OlMatrix(size_t rows = 0, size_t cols = 0)
    {
        m_node_pool = new Node[(rows + 10) * (cols + 10)];
        m_allocated_cnt = 0;
        if (rows > 0)
        {
            Node *pre_iter = &origin;
            for (size_t i = 0; i < rows; i++)
            {
                Node *node = NewNode();
                node->m_col_pre = pre_iter;
                pre_iter->m_col_next = node;
                m_row_heads.push_back(node);
                pre_iter = node;
            }
        }
        if (cols > 0)
        {
            Node *pre_iter = &origin;
            for (size_t i = 0; i < cols; i++)
            {
                Node *node = NewNode();
                node->m_row_pre = pre_iter;
                pre_iter->m_row_next = node;
                m_col_heads.push_back(node);
                pre_iter = node;
            }
        }
    }
    ~OlMatrix()
    {
        if (m_node_pool)
            delete m_node_pool;
    }

public:
    void DisconnectRow(Node *p)
    {
        auto l = p->m_row_pre, r = p->m_row_next;
        if (l)
            l->m_row_next = r;
        if (r)
            r->m_row_pre = l;
    }

    void DisconnectCol(Node *p)
    {
        auto l = p->m_col_pre, r = p->m_col_next;
        if (l)
            l->m_col_next = r;
        if (r)
            r->m_col_pre = l;
    }

    Node *NewNode()
    {
        return &m_node_pool[m_allocated_cnt++];
    }

    void Insert(Node *row_pre, Node *col_pre, Node *cur)
    {
        cur->m_row_pre = row_pre;
        cur->m_col_pre = col_pre;
        row_pre->m_row_next = cur;
        col_pre->m_col_next = cur;
    }
};

int visited_flags[30000];

/**
 * @brief
 *
 * @param entry entry node
 * @param flags an flags array which item need to be marked
 * @param fake_marked an ID need to be trated as marked
 * @return int
 * an extra cost when markedID merge with fakeID
 */
int SumAndMarkedBfs(deps_node *entry, int flags[], int fake_marked)
{
    int marked = entry->id;
    std::queue<deps_node *> que;
    que.push(entry);
    int total_cost = 0;
    while (!que.empty())
    {
        entry = que.front();
        que.pop();
        auto &flag = flags[entry->id];
        if (flag != -1 && (flag == marked || flag == fake_marked))
            continue;
        flag = marked;
        total_cost += entry->cost;
        for (auto next : entry->out_nodes)
            que.push(next);
        // {
        // if (flags[next->id] == -1 || (flags[next->id] != marked && flags[next->id] != fake_marked))
        // }
    }

    return total_cost;
}

/**
 * @brief
 * init martix, fill up matrix
 * This is upper triangular matrix
 *
 * @param cost_matrix
 * @param tree
 */
void InitCostMatrix(OlMatrix<int> &cost_matrix, DependsTree &tree)
{
    auto rooti_it = tree.root_nodes.begin();
    auto row_head_it = cost_matrix.m_row_heads.begin();
    auto col_head_it = cost_matrix.m_col_heads.begin();
    for (; row_head_it != cost_matrix.m_row_heads.end(); row_head_it++, rooti_it++, col_head_it++)
    {
        auto col_end = *col_head_it;
        while (col_end->m_col_next)
            col_end = col_end->m_col_next;

        // construct point on diagonal line
        auto point = cost_matrix.NewNode();
        cost_matrix.Insert(*row_head_it, col_end, point);
        // calculate data
        memset(visited_flags, 0xFF, sizeof(visited_flags));
        auto base_cost = point->data = SumAndMarkedBfs(*rooti_it, visited_flags, (*rooti_it)->id);
        (*rooti_it)->total_cost = base_cost;
        // std::cout << (*rooti_it)->id << " | " << (*rooti_it)->name << " | " << point->data << std::endl;
        // fill up right side
        col_end = col_end->m_row_next;
        auto row_end = point;
        auto rootj_it = rooti_it;
        rootj_it++;
        for (; col_end; row_end = row_end->m_row_next, col_end = col_end->m_row_next, rootj_it++)
        {
            point = cost_matrix.NewNode();
            cost_matrix.Insert(row_end, col_end, point);
            auto part_cost = SumAndMarkedBfs(*rootj_it, visited_flags, (*rooti_it)->id);
            // if ((*rooti_it)->id == 7 && (*rootj_it)->id == 8566)
            //     std::cout << part_cost << std::endl;
            point->data = base_cost + part_cost;
            // std::cout << "\t" << (*rootj_it)->id << " | " << (*rootj_it)->name << " | " << base_cost << "+" << part_cost << std::endl;
        }
    }
}

class WorkerPyramid
{
private:
    OlMatrix<int> *cost_matrix;
    DependsTree *tree;

public:
    // list<OlMatrix<int>::Node *> cost_threshold, cost_threshold_lower, cost_threshold_greater;
    list<deps_node *> workers;
    size_t worker_id;
    int maximun_cost = -1;

    WorkerPyramid(OlMatrix<int> *cost_matrix, DependsTree *tree) : cost_matrix(cost_matrix), tree(tree)
    {
        // find maximun in diagnal line
        for (auto head : cost_matrix->m_row_heads)
            maximun_cost = std::max(maximun_cost, head->m_row_next->data);
        std::cout << "maximun cost: " << maximun_cost / 100 << std::endl;
        // initialize lots of workers
        // each worker only have one root node in initilization
        auto id = worker_id = tree->max_id + 1;
        for (auto i : tree->root_nodes)
        {
            tree->AddNode(id, "worker", 0);
            tree->AddEdge(id, i->id);
            auto new_node = tree->GetNodeById(id);
            new_node->total_cost = i->total_cost;
            workers.push_back(new_node);
            id++;
        }
    }

    // iterate in matrix without diagnal line
    void ForEach(std::function<void(OlMatrix<int>::Node *, size_t, size_t)> const &lambda)
    {
        auto i = 0, j = 0;
        for (auto head : cost_matrix->m_row_heads)
        {
            j = 1;
            for (auto it = head->m_row_next->m_row_next; it; it = it->m_row_next, j++)
                lambda(it, i, j);
            i++;
        }
    }

    void Build()
    {
        while (cost_matrix->m_row_heads.size() > 1)
        {
            OlMatrix<int>::Node *best, *candidate_lower = nullptr, *candidate_greater = nullptr;
            // OPMZ: too slow
            ForEach([&](OlMatrix<int>::Node *node, auto i, auto j) {
                // if (i == 2791 && j == 150)
                // if (node->data == 10)
                // if (i == 5390 && j == 1)
                // {
                //     std::cout << node->data << ' ' << i << ' ' << j << std::endl;
                //     candidate_lower = node;
                // }
                if (node->data <= maximun_cost)
                    if (candidate_lower)
                        candidate_lower = std::max(candidate_lower, node, [](auto a, auto b) { return a->data < b->data; });
                    else
                        candidate_lower = node;
                else if (candidate_greater)
                    candidate_greater = std::min(candidate_greater, node, [](auto a, auto b) { return a->data < b->data; });
                else
                    candidate_greater = node;
            });
            best = candidate_lower ? candidate_lower : candidate_greater;
            std::cout << best->data / 100 << " : ";
            OlMatrix<int>::Node *it;
            auto worker_i_it = workers.begin();
            auto worker_j_it = workers.begin();
            auto cnt_i = 0, cnt_j = 0;
            for (it = best; it->m_row_pre; it = it->m_row_pre)
                ;
            // worker_j_it++, cnt_j++;
            // corresponds to worker_i
            auto best_row_headi = it;
            it = best->m_col_pre;
            for (; it->m_col_pre; it = it->m_col_pre)
            {
                // remove node from cost_matrix
                cost_matrix->DisconnectRow(it);
                // find worker
                worker_i_it++;
                cnt_i++;
                worker_j_it++;
                cnt_j++;
            }
            // remove node from m_col_heads
            cost_matrix->DisconnectRow(it);
            cost_matrix->m_col_heads.remove(it);
            for (it = best; it->m_col_next; it = it->m_col_next)
            {
                // remove node from cost_matrix
                cost_matrix->DisconnectRow(it);
                // find worker
                worker_j_it++;
                cnt_j++;
            }
            // this is another row head node
            // corresponds to worker_j
            auto best_row_headj = it->m_row_pre;
            cost_matrix->DisconnectCol(best_row_headj);
            cost_matrix->m_row_heads.remove(best_row_headj);
            for (it = best_row_headj->m_row_next; it; it = it->m_row_next)
            {
                // remove node from cost_matrix
                cost_matrix->DisconnectCol(it);
            }
            // merge worker i and j
            auto new_id = tree->max_id + 1;
            tree->AddNode(new_id, "worker", 0);
            tree->AddEdge(new_id, (*worker_i_it)->id);
            tree->AddEdge(new_id, (*worker_j_it)->id);
            std::cout << "worker id:(" << (*worker_i_it)->id << ',' << (*worker_j_it)->id << ")->" << new_id << ' ';
            // std::cout << cnt_i << '|' << cnt_j << ' ';
            std::cout << "cost:" << best_row_headi->m_row_next->data / 100 << '+' << best_row_headj->m_row_next->data / 100;
            *worker_i_it = tree->GetNodeById(new_id);
            workers.erase(worker_j_it);
            // update node in diagnal line
            memset(visited_flags, 0xFF, sizeof(visited_flags));
            auto cost_new = best_row_headi->m_row_next;
            auto base_cost = cost_new->data = SumAndMarkedBfs(*worker_i_it, visited_flags, (*worker_i_it)->id);
            maximun_cost = std::max(maximun_cost, base_cost);
            std::cout << "=" << cost_new->data / 100 << " remain workers:" << cost_matrix->m_row_heads.size() << " maxinum cost:" << maximun_cost / 100 << std::endl;
            (*worker_i_it)->total_cost = cost_new->data;
            // update nodes in row
            cnt_j = 0;
            for (it = cost_new->m_row_next, worker_j_it = worker_i_it; it; it = it->m_row_next)
            {
                worker_j_it++;
                cnt_j++;
                auto part_cost = SumAndMarkedBfs(*worker_j_it, visited_flags, (*worker_i_it)->id);
                it->data = base_cost + part_cost;
                // std::cout << "\t" << (*worker_j_it)->id << " | " << (*worker_j_it)->name << " | " << base_cost << "+" << part_cost << std::endl;
            }
            // update nodes in column
            cnt_j = 0;
            for (it = cost_new->m_col_pre, worker_j_it = worker_i_it; it->m_col_pre; it = it->m_col_pre)
            {
                cnt_j++;
                worker_j_it--;
                auto part_cost = SumAndMarkedBfs(*worker_j_it, visited_flags, (*worker_i_it)->id);
                it->data = base_cost + part_cost;
                // std::cout << "\t" << (*worker_j_it)->id << " | " << (*worker_j_it)->name << " | " << base_cost << "+" << part_cost << std::endl;
            }
            // return;
        }
    }

    string toJson(string id2name[])
    {
        json ans = json::array();
        std::queue<deps_node *> que;
        std::stringstream ss;
        que.push(*workers.begin());
        while (!que.empty())
        {
            auto worker = que.front();
            que.pop();
            if (worker->id < worker_id)
                // this is not worker
                continue;
            json j;
            ss.str("");
            ss << "worker" << worker->id;
            j["id"] = j["name"] = ss.str();
            auto data = json::object();
            data["type"] = "worker";
            data["cost"] = worker->cost;
            data["totalCost"] = worker->total_cost;
            data["numid"] = worker->id;
            j["data"] = data;
            auto adjacencies = json::array();
            for (auto i : worker->out_nodes)
            {
                que.push(i);
                ss.str("");
                if (i->id < worker_id)
                    ss << id2name[i->id];
                else
                    ss << "worker" << i->id;
                auto edge = json::object();
                edge["nodeTo"] = ss.str();
                edge["data"] = json::object({});
                adjacencies.push_back(edge);
            }
            j["adjacencies"] = adjacencies;
            ans.push_back(j);
        }
        return ans.dump(2);
    }
};

string BuildWorkerPyramid(string graph_json)
{
    auto graph = json::parse(graph_json);
    if (!graph.is_array())
        return "";
    std::cout << "constructing depends tree..." << std::endl;
    DependsTree tree;
    std::map<string, size_t> name2id;
    string id2name[30000];
    for (auto &i : graph)
    {
        // std::cout << i["data"]["numid"] << " " << i["name"] << " " << i["data"]["cost"] << std::endl;
        tree.AddNode(i["data"]["numid"], i["name"], i["data"]["cost"]);
        name2id[i["name"]] = i["data"]["numid"];
        id2name[i["data"]["numid"].get<int>()] = i["name"];
    }
    for (auto &i : graph)
    {
        if (i.count("adjacencies") == 0)
            continue;
        auto edges = i["adjacencies"];
        if (!edges.is_array())
            return "";
        auto from = i["data"]["numid"];
        for (auto &j : edges)
        {
            // std::cout << from << ' ' << name2id[j["nodeTo"]] << std::endl;
            tree.AddEdge(from, name2id[j["nodeTo"]]);
        }
    }
    tree.ExtractRootNodes();
    std::cout << "Initialize cost matrix..." << std::endl;
    OlMatrix<int> cost_matrix(tree.root_nodes.size(), tree.root_nodes.size());
    InitCostMatrix(cost_matrix, tree);
    std::cout << "root nodes: " << tree.root_nodes.size() << std::endl;
    std::cout << "matrix rows: " << cost_matrix.m_row_heads.size() << std::endl;
    // preparation has been done.
    // Let's start to build worker pyramid
    WorkerPyramid wp(&cost_matrix, &tree);
    wp.Build();
    auto ans = wp.toJson(id2name);
    std::cout << "Done Done Done" << std::endl;
    return ans;
}
