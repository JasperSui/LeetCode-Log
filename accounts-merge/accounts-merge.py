class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            parent[find(i)] = find(j)
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(email, account[1])
    
        tree = defaultdict(list)
        for email in parent.keys():
            tree[find(email)].append(email)

        return [[email_to_name[root]] + sorted(emails) for root, emails in tree.items()]
        
        
#         d1 = defaultdict(list)
#         d2 = defaultdict(set)
#         for account in accounts:
#             name = account[0]
#             mails = account[1:]
                
#             if all(mail not in d2[name] for mail in mails):
#                 d1[name].append(set(mails))
#             else:
#                 inner_mails = d1[name]
#                 for mail_set in inner_mails:
#                     print(mail_set)
#                     if any(mail in mail_set for mail in mails):
#                         mail_set.update(set(mails))
#             for mail in mails:
#                 d2[name].add(mail)
#         print(d1)
                
#         res = []
#         for name, d3 in d1.items():
#             for mails in d1[name]:
#                 mails = sorted(list(mails))
#                 account = [name]
#                 account.extend(mails)
#                 res.append(account)
#         return res