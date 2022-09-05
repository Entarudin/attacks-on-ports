from models import Target, Host


class TargetService:
    def create_target(
            self,
            ip_address: str,
            port_id: str,
            status: str,
            service: str,
            protocol: str,
    ):
        target = Target()
        target.ip_address = ip_address
        target.port_id = port_id
        target.status = status
        target.service = service
        target.protocol = protocol
        return target

    def cast_hosts_in_targets(self, hosts: list[Host]) -> list[Target]:
        result = []
        for item in hosts:
            for port in item.ports:
                target = self.create_target(
                    item.ip_address,
                    port.port_id,
                    port.status,
                    port.service,
                    port.protocol
                )
                result.append(target)
        return result