from nameko.rpc import rpc, RpcProxy

class Birds:
    name = "birds"

    @rpc
    def get(self):
        return {'name':'Pigeon'}
