from pants_test.pants_run_integration_test import PantsRunIntegrationTest

class NodeThriftLibraryIntegrationTest(PantsRunIntegrationTest):

  def test_node_install_codegen(self):
    command = ['node-install', 'contrib/node/examples/src/node/node-thrift-test/']
    pants_run = self.run_pants(command=command)
    self.assert_success(pants_run)

  def test_gen_thrift_node_codegen(self):
    command = ['gen.node-thrift', 'contrib/node/examples/src/node/node-thrift-test/']
    pants_run = self.run_pants(command=command)
    self.assert_success(pants_run)

