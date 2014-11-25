#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from java.util import HashSet

def containers():
    result = HashSet()
    for _delta in deltas.deltas:
        deployed = _delta.deployedOrPrevious
        current_container = deployed.container
        if deployed.hasProperty('restartContainer'):
            restartContainer = deployed.restartContainer
            if restartContainer and _delta.operation != "NOOP" and (current_container.type in ["jbossdm.Domain","jbossdm.StandaloneServer","jbossdm.Profile"]):
                result.add(current_container)
    return result


for container in containers():
    context.addStep(steps.os_script(
        description="Stopping server %s" % container.name,
        order=20,
        script="jbossdm/stop",
        freemarker_context={'container': container},
        target_host=container.host)
    )
    context.addStep(steps.os_script(
        description="Starting server %s" % container.name,
        order=80,
        script="jbossdm/start",
        freemarker_context={'container': container},
        target_host=container.host))