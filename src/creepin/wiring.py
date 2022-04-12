from dependency_injector import containers, providers


Container = containers.DynamicContainer()

#def wire(_db):
#    global Container
#    Container.db = providers.Factory(_db.Session)
#    Container.closed_db = providers.Resource(_db.get_closed_db)
#    #Container.wire(modules=modules)
#    #Container.wire(modules=["creepin.crud"] + modules)


#DEFAULT_MODULES = [crud]

#Container = containers.DynamicContainer()
### Need placeholders until wire is called
#Container.db = None
#Container.closed_db = None

#class Container(containers.DeclarativeContainer):
#    config = providers.Configuration()
#
#    # Do not use this with the Closing directive
#    #db = providers.Factory(SessionLocal)
#    db = None
#
#    # For use with Closing.
#    # Use only with scoped_session thread-local scope.
#    #closed_db = providers.Resource(get_closed_db)
#    closed_db = None



#def wire(modules=None):
#    if modules is None:
#        modules = DEFAULT_MODULES
#    container = Container()
#    container.init_resources()
#    container.wire(modules=modules)


#def wire(db_obj, modules=None):
#    if modules is None:
#        modules = DEFAULT_MODULES
#    container = Container()
#    container.db = providers.Factory(db_obj.Session)
#    container.closed_db = providers.Resource(db_obj.get_closed_db)
#    container.wire(modules=modules)




