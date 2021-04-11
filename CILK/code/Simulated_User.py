import random, requests


def init_simulated_user(path, user_node_index, user_rel_index):
    rel_file = open(path, 'r').readlines()
    print(('User KB rels.: ', len(rel_file)))

    # rel = rel_file[0].split('--->')[0]
    # rel = rel.replace('/', '_')
    #
    # nodes = rel_file[0].split('--->')[1].split('##')
    # nodes.remove(nodes[len(nodes) - 1])
    #
    # # dinh nghua user_rel_index
    # if rel in user_rel_index:
    #    user_rel_index[rel].extend(nodes)
    # else:
    #    user_rel_index[rel] = nodes
    #
    # # Cac cap (h,r,t) voi mot doi tuong bi khuyet
    # for j in range(0, len(nodes), 1):
    #     source = nodes[j].split('-;-')[0].strip()
    #     target = nodes[j].split('-;-')[1].strip()
    #
    #     print("J: ", j)
    #     print("source: ", source)
    #     print("target: ", target)
    #
    #     # For Source Node  ...
    #     if source in user_node_index:
    #         node_rel_pairs = user_node_index[source]
    #
    #         if target in node_rel_pairs:
    #             if rel not in node_rel_pairs[target]:
    #                 node_rel_pairs[target].append(rel)
    #         else:
    #             node_rel_pairs[target] = [rel]
    #         user_node_index[source] = node_rel_pairs
    #     else:
    #         node_rel_pairs = {target: [rel]}
    #         user_node_index[source] = node_rel_pairs
    #     #


    for i in range(0, len(rel_file), 1):
        rel = rel_file[i].split('--->')[0]
        rel = rel.replace('/', '_')

        nodes = rel_file[i].split('--->')[1].split('##')
        nodes.remove(nodes[len(nodes) - 1])

        if rel in user_rel_index:
           user_rel_index[rel].extend(nodes)
        else:
           user_rel_index[rel] = nodes

        for j in range(0, len(nodes), 1):
            source = nodes[j].split('-;-')[0].strip()
            target = nodes[j].split('-;-')[1].strip()

            # For Source Node  ...
            if source in user_node_index:
                node_rel_pairs = user_node_index[source]

                if target in node_rel_pairs:
                    if rel not in node_rel_pairs[target]:
                        node_rel_pairs[target].append(rel)
                else:
                    node_rel_pairs[target] = [rel]
                user_node_index[source] = node_rel_pairs
            else:
                node_rel_pairs = {target: [rel]}
                user_node_index[source] = node_rel_pairs

            # For Target Node ...
            if target in user_node_index:
                node_rel_pairs = user_node_index[target]

                if source in node_rel_pairs:
                    if rel + '-inv' not in node_rel_pairs[source]:
                        node_rel_pairs[source].append(rel + '-inv')
                else:
                    node_rel_pairs[source] = [rel + '-inv']
                user_node_index[target] = node_rel_pairs
            else:
                node_rel_pairs = {source: [rel + '-inv']}
                user_node_index[target] = node_rel_pairs


class Simulated_User(object):
    user_rel_index = {}
    user_node_index = {}

    def __init__(self, path, KB=None):
        init_simulated_user(path, self.user_node_index, self.user_rel_index)

        self.KB=KB
        self.number_clues_asked = 0
        self.number_clues_answered = 0
        self.number_conn_link_query_asked = 0
        self.number_conn_link_query_answered = 0
        self.query_list={}
        self.user_response_prob = 1.0
        print(('user interaction: ', self.user_response_prob))

    def reset_counters(self):
        self.number_clues_asked = 0
        self.number_clues_answered = 0
        self.number_conn_link_query_asked = 0
        self.number_conn_link_query_answered = 0

    def Ask_Simulated_User_For_Example(self, rel, num_clues = 1):  # for unknown relations.....
        self.number_clues_asked += 1
        if rel in self.user_rel_index and len(self.user_rel_index[rel]) > 0:
            clue_set = random.sample(self.user_rel_index[rel], min(len(self.user_rel_index[rel]), num_clues))
            self.number_clues_answered += 1
            return {(example.split('-;-')[0].strip(), example.split('-;-')[1].strip()) for example in clue_set}
        else:
            return {}

    def Ask_Simulated_User_For_connecting_link(self, unk_cpt, num_facts = 3):  # To connect unknown concepts with KG for reasoning
        self.query_list[unk_cpt] = ''
        self.number_conn_link_query_asked += 1

        response_set = set()
        if unk_cpt in self.user_node_index:
            node_rel_pairs = self.user_node_index[unk_cpt]
            target_nodes = random.sample(list(node_rel_pairs.keys()), int(min(len(list(node_rel_pairs.keys())), num_facts)))

            for t_node in target_nodes:
                link = random.choice(self.user_node_index[unk_cpt][t_node])
                response_set.add((unk_cpt, link, t_node))

            self.number_conn_link_query_answered += 1
        return response_set

if __name__ == "__main__":
    path = '/Users/taanhtuan/Desktop/workproject/CILK/resource_5/user_wordNet0.txt'
    user = Simulated_User(path)
