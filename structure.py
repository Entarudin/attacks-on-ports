from translators import (
    PortTranslator,
    HostTranslator,
    NetworkTranslator,
    ShellCommandTranslator,
    ListTranslator,
    AttackTranslator,
    TargetTranslator,
    ArpTranslator
)

from services import (
    InvokerShellCommandService,
    NetworkService,
    JsonService,
    AttackService,
    TargetService,
    ResultAttackService,
    ScapyService
)

from wrappers import MultiprocessingAttacksWrapper

port_translator = PortTranslator()
ports_translator = ListTranslator(port_translator)

host_translator = HostTranslator(ports_translator)
hosts_translator = ListTranslator(host_translator)

network_translator = NetworkTranslator(hosts_translator)
network_service = NetworkService()

shell_command_translator = ShellCommandTranslator()
invoker_shell_command_service = InvokerShellCommandService()

target_translator = TargetTranslator()
targets_translator = ListTranslator(TargetTranslator)

attack_translator = AttackTranslator(target_translator)
attacks_translator = ListTranslator(attack_translator)

arp_translator = ArpTranslator()

json_service = JsonService(attacks_translator)
target_service = TargetService()
result_attack_service = ResultAttackService()


multiprocessing_attack_wrapper = MultiprocessingAttacksWrapper()

attack_service = AttackService(
    shell_command_translator,
    invoker_shell_command_service,
    target_service,
    result_attack_service,
    multiprocessing_attack_wrapper
)

scapy_service = ScapyService()

