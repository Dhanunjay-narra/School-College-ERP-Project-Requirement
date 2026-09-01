import 'package:flutter/material.dart';

class ParentDashboardScreen extends StatelessWidget {
  const ParentDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Parent Portal')),
      body: const Center(child: Text('Ward Overview & Fee Notifications')),
    );
  }
}
