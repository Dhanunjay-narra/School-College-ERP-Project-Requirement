import 'package:flutter/material.dart';
import 'screens/student_dashboard.dart';

void main() {
  runApp(const ERPMobileApp());
}

class ERPMobileApp extends StatelessWidget {
  const ERPMobileApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Apex ERP Mobile',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF0284C7)),
        useMaterial3: true,
      ),
      home: const StudentDashboardScreen(),
    );
  }
}
