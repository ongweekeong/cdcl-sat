from clause import Clause
from copy import copy

class Form():
    def __init__(self, clauses):
        self._clauses = clauses
        self._when_removed = [-1 for x in clauses]
        self._length = len(clauses)
        self._marked = set()

    def all_clauses(self):
        return map(
            lambda i: self._clauses[i],
            filter(
                lambda i: self._when_removed[i] == -1,
                range(len(self._clauses))
            )
        )
    
    def all_clauses_backwards(self):
        return map(
            lambda i: self._clauses[i],
            filter(
                lambda i: self._when_removed[i] == -1,
                reversed(range(len(self._clauses)))
            )
        )
    
    def add_clause(self, c):
        c.id = len(self._clauses)
        self._clauses.append(c)
        self._when_removed.append(-1)
        self._length += 1

    def __len__(self):
        return self._length
    
    def remove_clause_id(self, id, level):
        self._when_removed[id] = level
        self._length -= 1
        if level == 0:
            self._marked.add(id)
    
    def reset_to_level(self, level):
        for i in range(len(self._clauses)):
            if self._when_removed[i] > level:
                self._when_removed[i] = -1
                self._length += 1
            if self._when_removed[i] == -1:
                self._clauses[i].reset_to_level(level)
    
    def __str__(self):
        return str(self.all_clauses())

    # not exactly "last" - there's no order to the lits in a clause.
    def last_lit(self):
        for i in reversed(range(len(self._clauses))):
            if self._when_removed[i] == -1:
                clause = self._clauses[i]
                break
        if clause:
            return list(clause.all_literals())[-1]
        else:
            return None

    def permanently_forget_clauses(self, max_id, lem_count):
        
        
        
        # TODO
        #return














        if lem_count < 20:
            return
        for i in range(max_id, self._length-19):
            if self._when_removed[i] == -1 and len(self._clauses[i]) > 4:
                self.remove_clause_id(i, -99)
                self._marked.add(i)
        if len(self._marked) > 0:
            self._clauses = [self._clauses[i] for i in range(len(self._clauses)) if not i in self._marked]
            self._when_removed = [self._when_removed[i] for i in range(len(self._when_removed)) if not i in self._marked]
            for i in range(len(self._clauses)):
                self._clauses[i].id = i
            self._marked = set()
