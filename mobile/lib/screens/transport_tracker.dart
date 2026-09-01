import 'package:flutter/material.dart';

class TransportTrackerScreen extends StatelessWidget {
  const TransportTrackerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Live Bus GPS Tracking')),
      body: const Center(child: Text('Bus Route #01 — ETA 12 mins')),
    );
  }
}
