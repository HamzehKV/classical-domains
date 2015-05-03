domains = [
{'description': 'Nomystery is a transportation domain designed to study resource constrained planning. In this domain, a truck moves in a weighted graph; a set of packages must be transported between nodes; actions move along edges, and load/unload packages; each move consumes the edge weight in fuel. In brief, Nomystery is a straightforward problem similar to the ones contained in many IPC benchmarks. Its key feature is that it comes with a domain-specific optimal solver allowing to control the constrainedness of the resources. The generator first creates a random connected undirected graph with n nodes, and it adds k packages with random origins and destinations. The edge weights are uniformly drawn between 1 and an integer W. The optimal solver computes the minimum required amount of fuel M, and the initial fuel supply is set to [C xM], where C >=1 is a (float) input parameter of the generator. The parameter C denotes the ratio between the available fuel vs. the minimum amount required. The problem becomes more constrained when C approaches 1.',
 'ipc': '2011',
 'name': 'nomystery',
 'problems': [('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p01.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p02.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p03.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p04.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p05.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p06.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p07.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p08.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p09.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p10.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p11.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p12.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p13.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p14.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p15.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p16.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p17.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p18.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p19.pddl'),
              ('nomystery-sat11-strips/domain.pddl',
               'nomystery-sat11-strips/p20.pddl')]}
]